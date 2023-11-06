# opentelemetry

# Usage
##  install
```
pip install opentelemetry-distro opentelemetry-exporter-otlp
pip install opentelemetry-instrumentation-fastapi

opentelemetry-bootstrap --action=install
```

## configure
```
export OTEL_SERVICE_NAME="cloud-desk"
export OTEL_TRACES_EXPORTER="console,otlp"
export OTEL_METRICS_EXPORTER="console"
export OTEL_EXPORTER_OTLP_TRACES_ENDPOINT="http://localhost:4317"
export OTEL_EXPORTER_OTLP_PROTOCOL="grpc opentelemetry-instrument uvicorn main:app --host localhost --port 8000"




export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_REQUEST="content-type,custom_request_header"
export OTEL_INSTRUMENTATION_HTTP_CAPTURE_HEADERS_SERVER_RESPONSE="content-type,custom_response_header"

```

```
OTEL_SERVICE_NAME=cloudesk \
OTEL_TRACES_EXPORTER=console,otlp \
OTEL_METRICS_EXPORTER=console \
OTEL_EXPORTER_OTLP_TRACES_ENDPOINT=0.0.0.0:4317
opentelemetry-instrument \
    uvicorn main:app --host localhost --port 8000

```

## run
注意，不能使用重载模式`uvicorn main:app --reload`  
请使用`uvicorn main:app` 

# Reference
[opentelemetry-instrumentation-fastapi](https://opentelemetry-python-contrib.readthedocs.io/en/latest/instrumentation/fastapi/fastapi.html#usage)