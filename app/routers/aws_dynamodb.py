from settings.config import env, logger, templates
from fastapi import (
    APIRouter,
    UploadFile,
    File,
Form,
    HTTPException,
    Request,
)

from fastapi.responses import HTMLResponse, JSONResponse
from backend.dynamodb import create_tables
from services.song import create_song, get_song, get_songs, delete_song, update_song
from models.song import Song
from models.song import DeleteSong

router = APIRouter(prefix="/aws/dynamodb", tags=env.AWS_DYNAMODB_TAGS)


@router.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    return templates.TemplateResponse("aws/dynamodb.html", {"request": request})


@router.post("/init_db", response_class=JSONResponse)
def init_db(table_name: str = Form(None)):
    r = create_tables(table_name)
    return r



@router.get("/song", response_class=HTMLResponse)
async def show_songs(request: Request):
    response = get_songs()
    songs = []
    for i in response:
        songs.append(i)
    return templates.TemplateResponse("aws/dynamodb/song.html", {"request": request, "songs": songs})

@router.post("/song/create", response_model=Song)
def create(song: Song):
    return create_song(song.model_dump())


@router.get("/song/get/{id}")
def get_songId(id: str):
    return get_song(id)


@router.get("/song/all")
def get_all_song():
    return get_songs()


@router.delete("/song/delete")
def delete(song: DeleteSong):
    return delete_song(song.model_dump())


@router.put("/song/update")
def update(song: Song):
    return update_song(song.model_dump())
