"""Check planning-fixture arithmetic and encoded constraints, not health safety.

Standard library only. This utility is not the HeatOps application or planner.
"""
import json
import math
from pathlib import Path


def minutes(value):
    hour, minute = map(int, value.split(":"))
    assert 0 <= hour < 24 and 0 <= minute < 60
    return hour * 60 + minute


def overlap(a, b, c, d):
    return max(0, min(b, d) - max(a, c)) / 60


def verify(data):
    assert data["sourceMode"] == "synthetic"
    weather = data["weather"]["hourly"]
    assert [minutes(x["time"]) for x in weather] == list(range(0, 1440, 60))
    assert all(math.isfinite(x["apparent_temperature_c"]) for x in weather)
    threshold = data["policy"]["flagAtOrAbove"]
    flagged = [(minutes(x["time"]), minutes(x["time"]) + 60)
               for x in weather if x["apparent_temperature_c"] >= threshold]
    assert flagged == [(780, 840), (840, 900), (900, 960)]
    actual = {}
    for name, schedule in data["schedules"].items():
        total, exposure = 0.0, 0.0
        rest_intervals = []
        for crew_id, blocks in schedule["blocks"].items():
            crew = data["crews"][crew_id]
            intervals = [(minutes(b["start"]), minutes(b["end"])) for b in blocks]
            assert len(intervals) == 2
            assert all(end - start == 180 for start, end in intervals)
            assert intervals[1][0] - intervals[0][1] >= data["policy"]["minGapMinutes"]
            assert intervals[-1][1] - intervals[0][0] <= data["policy"]["maxShiftSpanMinutes"]
            if not crew["movable"]:
                assert blocks == data["schedules"]["baseline"]["blocks"][crew_id]
            for start, end in intervals:
                assert start >= max(minutes(schedule["gateOpen"]), minutes(crew["availableStart"]))
                assert end <= minutes(crew["availableEnd"])
                total += crew["count"] * (end - start) / 60
                exposure += crew["count"] * sum(overlap(start, end, a, b) for a, b in flagged)
            rest_intervals.append((intervals[0][1], intervals[1][0], crew["count"]))
        # This fixture assumes crews use shade during gaps between task blocks.
        for t in range(0, 1440):
            occupancy = sum(count for start, end, count in rest_intervals if start <= t < end)
            assert occupancy <= data["site"]["shadeCapacity"]
        expected = data["expected"][name]
        assert math.isclose(total, expected["taskWorkerHours"])
        assert math.isclose(exposure, expected["flaggedWorkerHours"])
        actual[name] = {"flaggedWorkerHours": exposure, "taskWorkerHours": total}
    difference = actual["baseline"]["flaggedWorkerHours"] - actual["revised"]["flaggedWorkerHours"]
    percent = 100 * difference / actual["baseline"]["flaggedWorkerHours"]
    assert math.isclose(difference, data["expected"]["revisedReductionWorkerHours"])
    assert math.isclose(percent, data["expected"]["revisedReductionPercent"])
    assert overlap(600, 780, 780, 960) == 0
    assert overlap(600, 810, 780, 960) == 0.5
    return {"schedules": actual, "revisedReductionPercent": round(percent, 1),
            "scope": "Synthetic planning arithmetic and encoded constraints only"}


if __name__ == "__main__":
    fixture = Path(__file__).resolve().parents[1] / "fixtures" / "delhi-heat-demo.json"
    print(json.dumps(verify(json.loads(fixture.read_text())), indent=2))
