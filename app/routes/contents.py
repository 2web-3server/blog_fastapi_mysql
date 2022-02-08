from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from starlette.responses import Response
from starlette.responses import JSONResponse
from app.database.conn import db, Base
from app.database.schema import Contents, Comments

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def contents(session: Session = Depends(db.session), ):
    # 글 전체목록 불러오기
    results = session.query(Contents).all()
    return results

@router.get("/{id}")
async def content(id: int, session: Session = Depends(db.session)):
    # 글 받아오기
    content = session.query(Contents).filter(Contents.id == id).first()
    comments = session.query(Comments).filter(Comments.content_id == id).all()
    result = {
        "content": content,
        "comments": comments
    }

    return result

class Item(BaseModel):
    title: str
    content: str
    blogger: str
    thumb: str = None

@router.post("/write")
async def content(item:Item,session: Session = Depends(db.session)):
    # 이미지 유무 판단
    if item.thumb is None:
        Contents(title= item.title, content=item.content, blogger=item.blogger).create(session, auto_commit=True)
        responses={200: {"status": "success", "detail":"No Thumb"}}
    else:
        Contents(title=item.title, content=item.content, blogger=item.blogger, thumb= item.thumb).create(session, auto_commit=True)
        responses={200: {"status": "success", "detail":"Thumb"}}
    return responses