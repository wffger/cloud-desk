
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

logger.info(env.AUTH_URL)
logger.info(env.AWS_REGION_NAME)
s3 = boto3.client(
    "s3",
    region_name=env.AWS_REGION_NAME,
    aws_access_key_id=env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
)

router = APIRouter(prefix="/aws/cloudwatch" , tags=env.AWS_CLOUDWATCH_TAGS)


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    logger.info('aws/cloudwatch/')
    return templates.TemplateResponse("aws/cloudwatch.html", {"request": request})

