# Docker

## Dockerfile

```Dockerfile
FROM python:3.12-slim

RUN apt-get update && apt-get upgrade -y && rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

The `apt-get upgrade` step applies current Debian security patches at build time, rather than relying on packages present when the base image was published. See [security.md](security.md) for the vulnerability findings this addressed.

## Build and run

```bash
docker build -t developer-toolkit-api .
docker run -p 8000:8000 developer-toolkit-api
```

To run in detached mode:

```bash
docker run -d -p 8000:8000 --name dev-tools-api developer-toolkit-api
```

To stop and remove the container:

```bash
docker stop dev-tools-api
docker rm dev-tools-api
```

## Docker Compose

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

Common commands:

```bash
docker-compose up --build         # Build and start
docker-compose down                # Stop
docker-compose build --no-cache    # Rebuild, ignoring cache
```
