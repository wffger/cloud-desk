# 简介
[Uptrace](https://uptrace.dev/)是一个基于OpenTelemetry的可观测平台。

## 修改入口文件
新的main.py
```python
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import (
    home,
    aws_cloudwatch,
    aws_ec2,
    aws_s3,
    aws_dynamodb,
)
from settings.config import env, logger
import uptrace
from opentelemetry import trace
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor

app = FastAPI()
app.include_router(home.router)
app.include_router(aws_cloudwatch.router)
app.include_router(aws_ec2.router)
app.include_router(aws_s3.router)
app.include_router(aws_dynamodb.router)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")

logger.info("print otel info:")
logger.info("-- UPTRACE_DSN: %s", env.UPTRACE_DSN)
logger.info("-- AWS_S3_BUCKET: %s", env.AWS_S3_BUCKET)
uptrace.configure_opentelemetry(
    # Copy DSN here or use UPTRACE_DSN env var.
    dsn=env.UPTRACE_DSN,
    service_name=env.SERVICE_NAME,
    service_version=env.SERVICE_VERSION,
    deployment_environment=env.DEPLOYMENT_ENVIRONMENT,
)
tracer = trace.get_tracer("app_or_package_name", "1.0.0")

FastAPIInstrumentor.instrument_app(app)

```