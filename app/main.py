from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from routers import (
    home,
    aws_cloudwatch,
    aws_ec2,
    aws_s3,
    aws_dynamodb,
)

app = FastAPI()
app.include_router(home.router)
app.include_router(aws_cloudwatch.router)
app.include_router(aws_ec2.router)
app.include_router(aws_s3.router)
app.include_router(aws_dynamodb.router)
app.mount("/static", StaticFiles(directory="frontend/static"), name="static")


