# Developer Toolkit API

The Developer Toolkit API is a modular backend service built with FastAPI. It provides a growing set of utility endpoints that simplify common developer tasks, such as JSON formatting and string manipulation. This project is designed for ease of use, extensibility, and clean code organization.

## Features

- JSON prettifier (minify and beautify raw JSON)
- Modular, scalable route structure
- Automatically generated OpenAPI documentation
- Lightweight and fast with FastAPI
- Unit testing with `pytest`
- Optional containerization with Docker
- CI-ready with GitHub Actions (coming soon)

## Project Structure

```c#
developer-toolkit-api/
├── app/
│   ├── main.py
│   └── routes/
│       └── json_tools.py
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
Comming soon in the `tests/` durectory using `pytest`.
```bash
pytest
```

## API documentation

FastAPI automatically generates two UIs:

- Swagger UI: `http://localhost:8000/docs`

- Redoc UI: `http://localhost:8000/redoc`

## Available routes 

`GET / `
Returns a welcome message. 

`POST /tootls/json/prettify `
Description: Beautifies a raw JSON string
Request Body:
```json
{
  "content": "{\"key\":\"value\"}"
}
```
Response:
```json
{
  "prettified": "{\n    \"key\": \"value\"\n}"
}
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