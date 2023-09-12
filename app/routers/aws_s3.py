from typing import Annotated
from fastapi import (
    APIRouter,
    UploadFile,
    File,
    Cookie,
    Form,
    HTTPException,
    Request
)

from fastapi.responses import HTMLResponse
import boto3
from botocore.exceptions import ClientError

from settings.config import env, logger, templates

logger.debug(f'env.AWS_ACCESS_KEY_ID: {env.AWS_ACCESS_KEY_ID}')


router = APIRouter(prefix="/aws/s3" , tags=env.AWS_S3_TAGS)

@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("aws/s3.html", {"request": request})


@router.post("/upload")
async def upload_file(check_cookie: bool = Form(False), file: UploadFile = File(...), aws_region_name: Annotated[str | None, Cookie()] = None, aws_access_key_id: Annotated[str | None, Cookie()] = None, aws_secret_access_key: Annotated[str | None, Cookie()] = None):
    try:
        if check_cookie:
            logger.debug("使用cookie")
            s3 = boto3.client(
                "s3",
                region_name=aws_region_name,
                aws_access_key_id=aws_access_key_id,
                aws_secret_access_key=aws_secret_access_key,
            )
        else:
            logger.debug("不使用cookie")
            s3 = boto3.client(
                "s3",
                region_name=env.AWS_REGION_NAME,
                aws_access_key_id=env.AWS_ACCESS_KEY_ID,
                aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
            )
        s3.upload_fileobj(file.file, env.AWS_S3_BUCKET, file.filename)
        return {"文件已上传": file.filename}
    except ClientError as error:
        if error.response['Error']['Code'] == 'LimitExceededException':
            logger.warning('API call limit exceeded; backing off and retrying...')
        else:
            raise HTTPException(status_code=500, detail=error)

