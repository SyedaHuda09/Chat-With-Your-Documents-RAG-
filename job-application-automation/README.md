# AI Job Application Automation — n8n + LLM + Real Test UI

A portfolio-ready automation system that turns a job description into a structured application workflow.

## What it demonstrates
- n8n workflow orchestration
- LLM-ready job analysis
- Job/resume fit scoring
- Tailored cover-letter generation
- Human-in-the-loop approval
- REST/webhook integration
- Browser UI for live testing

## Architecture
Browser UI -> n8n Webhook -> Normalize -> Fit Scorer -> Application Draft -> Human Approval

## Run the UI
Open `ui/index.html` in a browser. Demo Mode works without API keys.
To connect n8n, paste your webhook URL and run the workflow.

## n8n
Import `n8n/job-application-automation.json` into n8n. Configure your LLM/provider separately and never commit secrets.

The workflow deliberately stops at human approval instead of silently submitting applications.

## Production extensions
PostgreSQL, Redis, FastAPI, Docker, LangSmith/OpenTelemetry, ATS integrations and authenticated approval endpoints.

> Demo Mode is deterministic and does not submit real applications. Production integrations should respect job-board terms, employer policies and rate limits.
