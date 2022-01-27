from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from starlette.responses import Response

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
