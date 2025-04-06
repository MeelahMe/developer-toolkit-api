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

You can view the results in the Actions tab of the repository.

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