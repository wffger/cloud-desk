from fastapi import APIRouter, Request, Response, Form
from fastapi.responses import HTMLResponse, JSONResponse

from settings.config import env, logger, templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/info", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})



@router.get("/aws", response_class=HTMLResponse)
async def show_aws(request: Request):
    return templates.TemplateResponse("aws/aws.html", {"request": request})

@router.post("/aws", response_class=HTMLResponse)
async def set_aws(aws_access_key_id: str = Form(), aws_secret_access_key: str = Form(), aws_region_name: str = Form()):
    response = JSONResponse(content={"message":"成功设置AWS"})
    response.set_cookie(key="aws_access_key_id", value=aws_access_key_id)
    response.set_cookie(key="aws_secret_access_key", value=aws_secret_access_key)
    response.set_cookie(key="aws_region_name", value=aws_region_name)
    return response

