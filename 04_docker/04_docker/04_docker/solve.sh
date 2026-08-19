#!/bin/bash
cat > docker-compose.yml << 'EOF'
services:
  app:
    build:.
    ports:
      - "8000:8000"
    depends_on:
      redis:
        condition: service_healthy
  redis:
    image: redis:7-alpine
    healthcheck:
      test: ["CMD", "redis-cli", "ping"]
      interval: 2s
      timeout: 3s
      retries: 10
EOF
