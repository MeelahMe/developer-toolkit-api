# Developer Toolkit API

The Developer Toolkit API is a modular backend service built with FastAPI. It provides a growing set of utility endpoints to simplify common developer tasks, such as JSON formatting and string manipulation. This project is designed for clarity, scalability, and easy testing.

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
Then run 

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

## BUild the Docker image

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


## Comming soon

- UUID Generator

- Timestamp Converter

- Base64 Encoder/Decoder

- URL Encoder/Decoder

- IP Info Lookup

- Password Generator

## License 
This project is licensed under the MIT License.