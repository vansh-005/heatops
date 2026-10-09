# Sources and evidence boundaries

URLs are primary references; SDK and account configuration must still be verified during implementation.

## Event

- Environmental Hacks: https://www.wemakedevs.org/aws/env — Heat and Water track and event context.
- Tour rules: https://www.wemakedevs.org/aws/rules — project provenance, AI-tool disclosure, and attribution requirements.

## Agent and AWS

- Strands Bedrock provider: https://strandsagents.com/docs/user-guide/sdk/model-providers/amazon-bedrock/ — provider configuration and tool-capable model integration. Documentation navigation and interfaces can evolve; pin the tested dependency and use its matching docs.
- AWS introduction to Strands: https://aws.amazon.com/blogs/opensource/introducing-strands-agents-an-open-source-ai-agents-sdk/ — AWS open-source origin and tool-use approach.
- Bedrock models: https://docs.aws.amazon.com/bedrock/latest/userguide/models.html — current capability/region information; not proof this user's account has access.
- Inference profiles: https://docs.aws.amazon.com/us_en/bedrock/latest/userguide/inference-profiles-support.html — profile availability and destination-region permission considerations.
- Lambda/SQS configuration: https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-configure.html — queue visibility guidance and event-source configuration.
- Lambda SQS failures: https://docs.aws.amazon.com/lambda/latest/dg/services-sqs-errorhandling.html — retry and batch failure behavior. Our batch size 1 simplifies handling; idempotency remains necessary.

## Weather

- Forecast API: https://open-meteo.com/en/docs — hourly forecast variables, time settings, units, and provider attribution. Live adapter documentation reference.
- Historical forecast: https://open-meteo.com/en/docs/historical-forecast-api — potential stretch data product. If historical forecast evidence is used later, verify initialization/lead-time semantics; do not assume a stitched archive is exactly what was known at a prior planning instant.
- Historical weather: https://open-meteo.com/en/docs/historical-weather-api — reanalysis is a different product from a contemporaneous forecast. The included synthetic fixture is not derived from either archive.

## Heat-screening boundary

- OSHA hazard recognition: https://www.osha.gov/heat-exposure/hazards — workplace heat assessment involves more than forecast temperature; WBGT incorporates factors absent from a simple weather threshold.
- CDC/NIOSH heat app: https://www.cdc.gov/niosh/heat-stress/communication-resources/app.html — an index alone cannot establish worker safety.

These US occupational resources inform the prototype's limitations; they are not presented as Indian legal requirements. The pack does not substantiate the earlier conversation's specific April 2026 government-advisory claim and does not use it in the pitch.

## What is our own design or illustrative data

The name, scenario, UI, 40°C apparent-temperature screening trigger, 30-minute gap, gate times, worker counts, task schedule, due times, region preference, run limits, and architecture are proposed design choices. They are not sourced safety guidance or measured customer outcomes. Arithmetic is reproducible with the included fixture checker.

