# Setup Guide

1. Infrastructure
```bash
cd terraform
terraform init
terraform apply
```

2. Environment
```bash
cp .env.example .env
# Edit .env with your values
```

3. Deploy
```bash
docker-compose up -d
```

4. Monitor
- Access dashboard: http://localhost:3000
- Metrics: http://localhost:8000/metrics
- Logs: /var/log/threat-intel.log