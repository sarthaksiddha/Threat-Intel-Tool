# Threat Intelligence API Documentation

## Authentication
All API endpoints require JWT authentication. 

```bash
# Get token
POST /token
Content-Type: application/x-www-form-urlencoded
username=user&password=pass

# Use token
GET /threats
Authorization: Bearer <token>
```

## Endpoints

### GET /threats
Retrieve all threat indicators.

### GET /analyze/{threat_id}
Analyze specific threat using AI.

### POST /integrate
Add new threat intelligence source.

## Error Codes
- 401: Unauthorized
- 404: Resource not found
- 500: Server error