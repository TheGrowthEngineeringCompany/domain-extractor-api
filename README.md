# Domain Extraction API.

A simple API you can spin up on Heroku, AWS Lambda that takes in a raw URL, and spits back a purified domain.

Built with tldrextract + FastAPI + Past headaches with data cleanliness.

Test it out on:

GET
https://domain-extractor.reconfigured.io/extract?url=http://wwW.paddle.com/en?utm_campaign=whatever&hello=world

Much love,
@thesnappingdog

## Examples:

[see examples folder](../blob/main/examples)

- n8n workflow
- HubSpot Workflows

## Setup

To run in DEV mode:

```
python3 -m venv venv
source venv/bin.activate
pip install
uvicorn app.server:app --reload
```

Run tests with `python -m pytest tests/`
