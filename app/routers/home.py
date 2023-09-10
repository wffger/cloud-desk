from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse

from settings.config import env, logger, templates

router = APIRouter()


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/info", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("item.html", {"request": request})
