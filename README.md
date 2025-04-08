![Build](https://img.shields.io/github/actions/workflow/status/MeelahMe/developer-toolkit-api/ci.yml?label=build&logo=github)
![Python](https://img.shields.io/badge/python-3.9+-blue?logo=python&logoColor=white)
![Tests](https://img.shields.io/badge/tests-pytest-green?logo=pytest)

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

## Comming soon

- URL Encoder/Decoder
- IP Info Lookup

## License 
This project is licensed under the MIT License.