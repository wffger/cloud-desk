
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

logger.debug('env.AWS_ACCESS_KEY_ID: ', env.AWS_ACCESS_KEY_ID)
s3 = boto3.client(
    "s3",
    region_name=env.AWS_REGION_NAME,
    aws_access_key_id=env.AWS_ACCESS_KEY_ID,
    aws_secret_access_key=env.AWS_SECRET_ACCESS_KEY,
)

router = APIRouter(prefix="/aws/s3" , tags=env.AWS_S3_TAGS)

@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("aws/s3.html", {"request": request})


@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        s3.upload_fileobj(file.file, env.AWS_S3_BUCKET, file.filename)
        return {"文件已上传": file.filename}
    except ClientError as error:
        if error.response['Error']['Code'] == 'LimitExceededException':
            logger.warn('API call limit exceeded; backing off and retrying...')
        else:
            raise HTTPException(status_code=500, detail=error)

