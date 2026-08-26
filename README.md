[![Build](https://img.shields.io/github/actions/workflow/status/MeelahMe/developer-toolkit-api/ci.yml?label=build&logo=github)](https://github.com/MeelahMe/developer-toolkit-api/actions)
[![Python](https://img.shields.io/badge/python-3.12+-blue?logo=python)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/tests-pytest-green?logo=pytest)](https://github.com/MeelahMe/developer-toolkit-api)
[![Security Scan](https://img.shields.io/badge/security-trivy%20scanned-blue?logo=trivy)](https://github.com/MeelahMe/developer-toolkit-api/blob/master/.trivyignore)

A modern FastAPI microservice that helps developers with encoding, formatting, timestamp conversion, UUID generation, and more.

# Developer Toolkit API

The Developer Toolkit API is a modular backend service built with FastAPI. It provides a growing set of utility endpoints to simplify common developer tasks, such as JSON formatting and string manipulation. This project is designed for clarity, scalability, and easy testing.

## About FastAPI

[FastAPI](https://fastapi.tiangolo.com/) is a modern, high-performance web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed for speed and developer productivity, offering automatic data validation, interactive documentation via Swagger and ReDoc, and seamless integration with asynchronous Python code.

FastAPI is ideal for building APIs quickly while maintaining readability, robustness, and scalability. It is widely adopted for backend services, microservices, and machine learning model deployment.


## Features

- JSON prettifier (minify and beautify raw JSON)
- Modular route structure using FastAPI routers
- Auto-generated OpenAPI docs (Swagger UI and ReDoc)
- Unit tested with `pytest`
- Continuous integration using GitHub Actions
- Optional Docker setup (coming soon)

## Project Structure


```c#
developer-toolkit-api/
├── app/
│   ├── __init__.py
│   ├── main.py
│   └── routes/
│       └── json_tools.py
├── tests/
│   └── test_json_tools.py
├── .github/
│   └── workflows/
│       └── ci.yml
├── pytest.ini
├── requirements.txt
├── README.md
├── .gitignore
```

## Getting Started

### Clone the repository

```bash
git clone https://github.com/MeelahMe/developer-toolkit-api.git
cd developer-toolkit-api
```

## Set up a virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
## Install dependencies

```bash
pip install -r requirements.txt
```
## Running the APP

```bash
uvicorn app.main:app --reload
```
By default, the API will be available at:
`http://localhost:8000`

## Running tests
Unit tests are written with pytest.

To run tests locally:

```bash
`PYTHONPATH=$(pwd) pytest`
```
You can also use `pytest.ini` to simplify local test runs:

pytest.ini

```bash
[pytest]
python_paths = .
```
Then run:

```bash
pytest
```

## Continuous Integration

Tests automatically run on each push and pull request using GitHub Actions. The workflow is defined in .github/workflows/ci.yml.

To trigger a run:

    Push any commit

    Open a pull request

You can view the results in the **Actions** tab of the repository.

## API documentation

FastAPI automatically generates two UIs:

- Swagger UI: `http://localhost:8000/docs`

- Redoc UI: `http://localhost:8000/redoc`

## Available routes 

`GET / `
Returns a welcome message. 

`POST /tootls/json/prettify `
Description: Beautifies a raw JSON string
**Request Body**:
```json
{
  "content": "{\"key\":\"value\"}"
}
```
**Response**:
```json
{
  "prettified": "{\n    \"key\": \"value\"\n}"
}
```

## Running the App with Docker

You can run the Developer Toolkit API in an isolated container using Docker. This approach is recommended for local development and deployment because it ensures consistent environments across machines.

### Prerequisites

- [Docker Desktop](https://www.docker.com/products/docker-desktop) installed and running
- Clone the repository and navigate to the root directory

### Dockerfile

The project includes a `Dockerfile` that defines the container build steps:

```Dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

## Build the Docker image

Run this command from the project root:
```bash
docker build -t developer-toolkit-api .
```

This will: 

- Use Python 3.9 as the base image
- Install dependencies from requirements.txt
- Copy all app files into the container
- Run the FastAPI app using Uvicorn

## Run the Docker container

After the image is built, start a container: 
```bash
docker run -p 8000:8000 developer-toolkit-api
```

You can now access the API at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

To run in detached mode use this command: 
```bash
docker run -d -p 8000:8000 --name dev-tools-api developer-toolkit-api
```

## Stop and remove the container

```bash
docker stop dev-tools-api
docker rm dev-tools-api
```

## Optional: Adding .dockerignore
To reduce image size and exclude unnecessary files, use a  .dockerignore by adding this file in your root: 

```bash
__pycache__/
*.pyc
*.pyo
*.pyd
venv/
.env
*.log
.git/
.gitignore
tests/
```
This ensures only the necessary application files are included in your final image.

## Running with Docker Compose

You can also use Docker Compose to manage the application and future services like databases or caching layers. This is a scalable approach for development and deployment.

### docker-compose.yml

This file defines the API service and allows you to run it with a single command:

```yaml
version: '3.9'

services:
  api:
    build: .
    container_name: developer-toolkit-api
    ports:
      - "8000:8000"
    volumes:
      - .:/app
    command: uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```
## Running the Application

To build and start the service:

`docker-compose up --build`

Once running, the API will be available at:

    Swagger UI: `http://localhost:8000/docs`

    ReDoc: `http://localhost:8000/redoc`
    
## Common Commands

Stop the running services:

```bash
docker-compose down
```

Rebuild the image and restart:

```bash
docker-compose up --build
```

Rebuild without using cache:

```bash
docker-compose build --no-cache
```

## Benefits of Docker Compose

- Scales easily with additional services (e.g., databases, task queues)
- Defines infrastructure-as-code for local dev environments
- Simplifies team collaboration with one-command startup

## API Documentation

FastAPI automatically generates two UIs:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

---

## Route Overview

| Method | Endpoint                       | Description                |
|--------|--------------------------------|----------------------------|
| GET    | `/`                            | Root welcome message       |
| POST   | `/tools/json/prettify`         | Prettifies raw JSON input  |
| GET    | `/tools/uuid/generate`         | Generates a UUID v4        |
| POST   | `/tools/base64/encode`         | Encodes a string to Base64 |
| POST   | `/tools/base64/decode`         | Decodes a Base64 string    |
| POST   | `/tools/time/convert`          | Converts between UNIX timestamp and ISO date string |
| GET    | `/tools/password/generate`     | Generates a secure random password |

---

## Available Routes

### `GET /`

Returns a welcome message confirming the API is running.

---

### `POST /tools/json/prettify`

Formats a raw JSON string with proper indentation.

**Request Body**

```json
{
  "content": "{\"key\":\"value\"}"
}
```

**Response**

```json
{
  "prettified": "{\n    \"key\": \"value\"\n}"
}
```
## GET /tools/uuid/generate

Generates a random UUID (version 4).

**Response**

```json
{
  "uuid": "c3d1a60e-5f63-42a5-8469-789db166e1b9"
}
```
---

### `POST /tools/base64/encode`

Encodes a plain text string into Base64.

**Request Body**

```json
{
  "content": "hello world"
}
```
**Response**

```json
{
  "encoded": "aGVsbG8gd29ybGQ="
}
```

---

### `POST /tools/base64/decode`

Decodes a Base64-encoded string back to plain text.

**Request Body**

```json
{
  "encoded": "aGVsbG8gd29ybGQ="
}
```

**Response**

```json
{
  "decoded": "hello world"
}
```

---

### `POST /tools/time/convert`

Converts between a UNIX timestamp and an ISO 8601 date string.

You must provide **either** a `timestamp` or a `date_string`.

**Request Body (timestamp to date):**

```json
{
  "timestamp": 1609459200
}
```

**Response**:

```json
{
  "date_string": "2021-01-01T00:00:00"
}
```
**Request Body (date to timestamp)**:

```json
{
  "date_string": "2021-01-01T00:00:00"
}
```

**Response**:

```json
{
  "timestamp": 1609459200
}
```

---

### `GET /tools/password/generate`

Generates a secure, random password.

You can customize the password using query parameters:

**Query Parameters:**

| Name              | Type    | Default | Description                            |
|-------------------|---------|---------|----------------------------------------|
| `length`          | integer | `12`    | Desired length of the password (4–128) |
| `include_symbols` | boolean | `true`  | Include special characters             |
| `include_numbers` | boolean | `true`  | Include digits                         |
| `include_uppercase` | boolean | `true`  | Include uppercase letters              |
| `include_lowercase` | boolean | `true`  | Include lowercase letters              |

**Example Request**

```http
GET /tools/password/generate?length=16&include_symbols=false&include_numbers=true
```
**Response**

```json
{
  "password": "ab9ZxkwmT4rnqY1v"
}
```

## Security & Hardening

This project's CI/CD pipeline includes automated container vulnerability scanning using [Trivy](https://trivy.dev), integrated as a second GitHub Actions job that runs after tests pass.

### Why Trivy

Trivy scans the built Docker image for known vulnerabilities (CVEs) in both OS-level packages and Python dependencies, and fails the build (`exit-code: 1`) if any CRITICAL or HIGH severity issues are found with an available fix. This turns vulnerability scanning from a passive report into an enforced gate. A container with fixable critical or high vulnerabilities cannot pass CI.

### What was found and fixed

The first scan against the original `python:3.9-slim` image surfaced **78 vulnerabilities (6 CRITICAL, 72 HIGH)**, spanning both OS packages and Python dependencies. Root causes and fixes:

| Issue | Root Cause | Fix |
|---|---|---|
| Stale OS packages (util-linux, openssl core, libcap2, etc.) | Base image OS packages were outdated relative to available Debian security patches | Added `apt-get update && apt-get upgrade -y` to the Dockerfile to pull current patches at build time |
| Outdated Python version | `python:3.9-slim` blocked upgrading to a patched FastAPI/Starlette (FastAPI 0.129 and above requires Python 3.10 or higher) | Bumped base image to `python:3.12-slim` |
| Vulnerable Starlette (CVE-2026-48818, CVE-2026-54283) | Outdated FastAPI pinned an old Starlette transitively | Upgraded FastAPI to 0.141.1, which resolved to a patched Starlette (1.6.0) |
| CI and Dockerfile Python version mismatch | The GitHub Actions `test` job still specified Python 3.9 after the Dockerfile was upgraded to 3.12 | Synced both to Python 3.12 to prevent environment drift between test and build environments |

These changes resolved **61 of the 78 findings**.

### Remaining accepted risk

The remaining **17 vulnerabilities** (3 CRITICAL, 14 HIGH) are documented in [`.trivyignore`](.trivyignore). Each has no upstream fix available yet from Debian as of the scan date, and all affect OS utilities the application does not invoke directly (`perl`, `gzip`, `ncurses`, `acl`) rather than application code paths. This is a deliberate, documented risk acceptance, not a suppression of the scan, and is re-evaluated whenever the pipeline runs against a fresh vulnerability database.


## Secret Detection

I added [gitleaks](https://github.com/gitleaks/gitleaks) as another job in the pipeline. It scans the full commit history, not just the current code, looking for things like API keys or tokens that got committed by accident.

It runs on its own, separate from the test and container scan jobs. It doesn't need the app to actually build since it's just scanning text and git history, so there's no reason to make it wait in line behind the other jobs.

### Making sure it actually works

I didn't want to just write the YAML and assume it worked, so I tested it. I committed a fake AWS-key-shaped string on a throwaway branch to see if gitleaks would catch it. First run, it didn't, because I'd made the change to the workflow file locally but never actually committed it before pushing the test branch. So the job that was supposed to catch the fake secret wasn't even in the pipeline yet when it ran. Once I realized that, it made sense why it passed.

Somewhere in there I also ended up accidentally merging that test branch into master, fake secret and all. Nothing sensitive since it was a made-up key, not a real one, but I didn't want it sitting in the history like it belonged there. Cleaned it up with `git revert -m 1` instead of rewriting history, since the branch had already been pushed and reverting keeps an honest record of what happened rather than pretending it didn't.

After actually committing the workflow change to master, I reran everything and confirmed it worked: no leaks in the real codebase, and I'd already seen it correctly flag the fake one earlier.


## Static Code Analysis

I added [Semgrep](https://semgrep.dev) as a third security job in the pipeline. Where Trivy looks at the container image and gitleaks looks at git history, Semgrep actually reads the source code itself, including the workflow YAML and Dockerfile, looking for risky patterns.

It runs independently too, same as the secrets scan, since it doesn't need the app to build first.

### What it actually caught

First run turned up 8 findings, but they all traced back to the same underlying issue: every `uses:` line in my GitHub Actions workflow was pointing at a mutable tag or branch, things like `@v3` or `@master`, instead of a pinned commit. That matters because whoever controls those actions could, in theory, repoint the tag to different code later, and my pipeline would silently start running it. Semgrep's own rule flagged two real past incidents where exactly that happened.

I fixed it by pinning every action to its actual commit SHA, using `git ls-remote --tags` against each repo to get the real SHA rather than trusting a copy-pasted one. Ran into an interesting wrinkle along the way: some tags are "annotated," meaning they show up as two different SHAs when you look them up, and only one of them (the one marked `^{}`) is the actual commit you want. Took a minute to understand why that was happening, but now I know it for good.

## Pre-commit Hooks

On top of everything running in CI, I set up pre-commit hooks so the same kind of checks run locally, before a commit even happens, not just after I push and wait for the pipeline.

Right now it runs two things on every commit:
- gitleaks, same secret scanner as CI, catching a leaked key before it's ever pushed instead of after
- ruff, for linting and formatting, it replaced what used to take three separate tools (flake8, black, isort) and it's noticeably faster

The first time I ran it against the whole existing codebase, it reformatted 11 files. Nothing was broken, ruff just found real formatting drift that had built up over time and fixed it automatically. That's actually the setup working exactly as intended, catching something real on the very first run instead of sitting there doing nothing.

Worth being clear: pre-commit isn't a replacement for the CI checks, it can be skipped and it only runs on machines that have it installed. It's a faster first layer, CI is still the actual gate.

## Authentication

Every tool endpoint requires an API key, sent via the `X-API-Key` header. The root route (`/`) stays open without a key, useful as a lightweight health check.

Set your key in a `.env` file at the project root (see `.env.example` for the expected format), the app reads it at startup and rejects any request with a missing or incorrect key.

Example request:
```bash
curl -H "X-API-Key: your-key-here" http://localhost:8000/tools/uuid/generat #gitleaks:allowe
```

I built this with a single shared key rather than per-user keys, since this is a personal toolkit API, not a multi-tenant service. A production version handling real users would need per-key issuance, rotation, and probably rate limiting per key, none of which felt necessary here, but worth naming as the honest next step if this ever needed to support more than one person.

One thing I'd add for a more security-sensitive version of this: `secrets.compare_digest()` instead of a plain string comparison when checking the key, to avoid a timing attack where an attacker could theoretically infer how much of the key they got right based on how long the comparison takes. Low real risk for a project like this, but it's the kind of detail that matters more the higher the stakes get.

## Metrics

The API exposes a `/metrics` endpoint in Prometheus's standard text format, tracking total requests and request duration, broken down by method, path, and status code.

Unlike the tool endpoints, `/metrics` doesn't require an API key. This is deliberate: Prometheus's own scraper needs to hit this endpoint automatically and repeatedly, without a human involved, so requiring auth here would mean either hardcoding a key into monitoring infrastructure or building a separate exemption anyway. The standard real-world approach is to protect `/metrics` at the network level instead, firewall rules or internal-only routing, not application-level auth.

Example:
```bash
curl http://localhost:8000/metrics
```

Returns Prometheus exposition format, including built-in Python runtime metrics (garbage collection stats, interpreter info) alongside the custom `http_requests_total` and `http_request_duration_seconds` metrics this app defines.

### What I'd add next

- A Grafana dashboard reading from this endpoint, to actually visualize request rates and latency over time
- Alerting rules (e.g., error rate exceeding some threshold), the kind of thing this endpoint makes possible but doesn't do on its own

## License 
This project is licensed under the MIT License.
