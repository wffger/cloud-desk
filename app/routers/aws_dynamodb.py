
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    HTTPException,
    Request
)

from fastapi.responses import HTMLResponse
import boto3
from botocore.exceptions import ClientError

from settings.config import env, logger, templates

s3 = boto3.client(
    "s3",
    region_name=env.AWS_REGION_NAME,
    aws_access_key_id=env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
)

router = APIRouter(prefix="/aws/dynamodb" , tags=env.AWS_DYNAMODB_TAGS)


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("aws/dynamodb.html", {"request": request})

