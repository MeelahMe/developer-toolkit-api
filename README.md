[![Build](https://img.shields.io/github/actions/workflow/status/MeelahMe/developer-toolkit-api/ci.yml?label=build&logo=github)](https://github.com/MeelahMe/developer-toolkit-api/actions)
[![Python](https://img.shields.io/badge/python-3.12+-blue?logo=python)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-green?logo=pytest)](https://github.com/MeelahMe/developer-toolkit-api)
[![Security Scan](https://img.shields.io/badge/security-trivy%20scanned-blue?logo=trivy)](https://github.com/MeelahMe/developer-toolkit-api/blob/master/.trivyignore)

# Developer Toolkit API

Developer Toolkit API is a FastAPI microservice that provides a small set of developer utilities, including JSON formatting, UUID generation, Base64 encoding, timestamp conversion, and secure password generation. The service is built on a full DevSecOps pipeline: authentication, structured logging, Prometheus metrics, request persistence, and a four-tool security scanning stack enforced in both CI and local pre-commit hooks.

## About FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance Python web framework built on standard type hints. It provides automatic data validation and interactive documentation (Swagger UI and ReDoc).

## Documentation

| Area | Reference |
|---|---|
| Available routes and examples | [docs/routes.md](docs/routes.md) |
| Authentication | [docs/authentication.md](docs/authentication.md) |
| Security scanning (Trivy, gitleaks, Semgrep, Bandit) | [docs/security.md](docs/security.md) |
| Metrics and usage history | [docs/observability.md](docs/observability.md) |
| Docker and Docker Compose | [docs/docker.md](docs/docker.md) |
| Deployment (Terraform, AWS) | [docs/deployment.md](docs/deployment.md) |

## Project structure

```
developer-toolkit-api/
├── app/
│   ├── __init__.py
│   ├── main.py            # App instance, middleware, routes
│   ├── auth.py             # API key verification
│   ├── database.py         # SQLAlchemy engine and session setup
│   ├── models.py           # RequestLog model
│   ├── metrics.py          # Prometheus counters and histograms
│   ├── logging_config.py   # JSON log formatter
│   └── routes/
│       ├── json_tools.py
│       ├── uuid_tools.py
│       ├── base64_tools.py
│       ├── time_tools.py
│       └── password_tools.py
├── tests/
│   ├── conftest.py         # Shared client and auth fixtures
│   ├── test_main.py
│   └── test_*.py           # One file per route module
├── docs/                   # Detailed documentation (see table above)
├── .github/workflows/ci.yml
├── .trivyignore
├── .pre-commit-config.yaml
├── Dockerfile
├── requirements.txt         # Runtime dependencies
├── requirements-dev.txt     # Test, lint, and security tooling
└── README.md
```

## Getting started

Clone the repository and set up a virtual environment:

```bash
git clone https://github.com/MeelahMe/developer-toolkit-api.git
cd developer-toolkit-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
```

Configure environment variables (see [docs/authentication.md](docs/authentication.md) for details):

```bash
cp .env.example .env
```

Run the application:

```bash
uvicorn app.main:app --reload
```

The API is available at `http://localhost:8000`. Interactive documentation is available at `http://localhost:8000/docs`.

## Running tests

```bash
PYTHONPATH=$(pwd) pytest -v
```

## Continuous integration

Every push and pull request runs five checks in parallel: the test suite, container vulnerability scanning, secret detection, static analysis, and a Python security linter. See [docs/security.md](docs/security.md) for details, including vulnerabilities identified and resolved during development. The workflow is defined in `.github/workflows/ci.yml`.

## Route summary

| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/` | Welcome message (no authentication) |
| GET | `/metrics` | Prometheus metrics (no authentication) |
| GET | `/usage` | Recent request history (authentication required) |
| POST | `/tools/json/prettify` | Prettifies raw JSON |
| GET | `/tools/uuid/generate` | Generates a UUID v4 |
| POST | `/tools/base64/encode` | Encodes text to Base64 |
| POST | `/tools/base64/decode` | Decodes Base64 to text |
| POST | `/tools/time/convert` | Converts between timestamp and ISO date |
| GET | `/tools/password/generate` | Generates a secure password |

Full request and response examples are available in [docs/routes.md](docs/routes.md).

## License

This project is licensed under the MIT License.
