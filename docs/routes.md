# Route reference

All tool routes require an API key. See [authentication.md](authentication.md).

## `GET /`

Returns a welcome message. No authentication required.

## `POST /tools/json/prettify`

**Request:**
```json
{ "content": "{\"key\":\"value\"}" }
```

**Response:**
```json
{ "prettified": "{\n    \"key\": \"value\"\n}" }
```

## `GET /tools/uuid/generate`

**Response:**
```json
{ "uuid": "c3d1a60e-5f63-42a5-8469-789db166e1b9" }
```

## `POST /tools/base64/encode`

**Request:**
```json
{ "content": "hello world" }
```

**Response:**
```json
{ "encoded": "aGVsbG8gd29ybGQ=" }
```

## `POST /tools/base64/decode`

**Request:**
```json
{ "encoded": "aGVsbG8gd29ybGQ=" }
```

**Response:**
```json
{ "decoded": "hello world" }
```

## `POST /tools/time/convert`

Accepts either `timestamp` or `date_string`.

**Request (timestamp to date):**
```json
{ "timestamp": 1609459200 }
```

**Response:**
```json
{ "date_string": "2021-01-01T00:00:00" }
```

**Request (date to timestamp):**
```json
{ "date_string": "2021-01-01T00:00:00" }
```

**Response:**
```json
{ "timestamp": 1609459200 }
```

## `GET /tools/password/generate`

**Query parameters:**

| Name | Type | Default | Description |
|---|---|---|---|
| `length` | integer | 12 | Password length (4–128) |
| `include_symbols` | boolean | true | Include special characters |
| `include_numbers` | boolean | true | Include digits |
| `include_uppercase` | boolean | true | Include uppercase letters |
| `include_lowercase` | boolean | true | Include lowercase letters |

**Example request:**
GET /tools/password/generate?length=16&include_symbols=false

**Response:**  <!-- gitleaks:allow -->
```json
{ "password": "example-password-123" }
```
