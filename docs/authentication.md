# Authentication

All tool endpoints require an API key, sent using the `X-API-Key` header. The root route (`/`) and `/metrics` do not require a key: `/` serves as a lightweight health check, and `/metrics` must remain accessible to automated monitoring scrapers.

Set the key in a `.env` file at the project root. See `.env.example` for the expected format. The application reads this value at startup and rejects any request with a missing or incorrect key.

## Example request

```bash
curl -H "X-API-Key: your-key-here" http://localhost:8000/tools/uuid/generate  # gitleaks:allow
```

## Design notes

This project uses a single shared key rather than per-user keys, since it is a personal toolkit API rather than a multi-tenant service. A production deployment serving multiple users would require per-key issuance, rotation, and rate limiting.

Key comparison currently uses plain string equality rather than `secrets.compare_digest()`. This introduces a theoretical timing-attack surface: an attacker could, in principle, infer partial key matches from response time. Risk is low at this scale, but `compare_digest()` is recommended for any higher-stakes reuse of this pattern.
