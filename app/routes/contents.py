from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.schema import Contents, Comments, Category

router = APIRouter(
    prefix="/contents",
    tags=["contents"],
    responses={404: {"description": "Not found"}},
)


# All List
@router.get("/{blogger}/all")
async def contents(blogger: str, session: Session = Depends(db.session), ):
    # 글 전체목록 불러오기
    results = session.query(Contents).filter(Contents.blogger == blogger).all()
    return results


# All list in category
@router.get("/{blogger}/category/{category_name}")
async def contents_from_category(category_name: str, blogger: str, session: Session = Depends(db.session)):
    # 카테고리 명으로 카테고리 객체 조회
    category_id_res = session.query(Category).filter(Category.blogger == blogger, Category.name == category_name).all()
    # 조회되는 맨 처음 객체 선택
    category_id = category_id_res[0].id
    # 해당하는 카테고리에 속하는 모든 글 불러오기
    results = session.query(Contents).filter(Contents.category_id == category_id).all()
    return results


# Detail
@router.get("/{blogger}/id/{id}")
async def content(blogger: str, id: int, session: Session = Depends(db.session)):
    # 글 받아오기
    content = session.query(Contents).filter(Contents.id == id).first()
    comments = session.query(Comments).filter(Comments.content_id == id).all()
    result = {
        "content": content,
        "comments": comments
    }

    return result


class PostModel(BaseModel):
    title: str
    content: str
    blogger: str
    thumb: str = None


@router.post("/write")
async def content(item: PostModel, session: Session = Depends(db.session)):
    print(item)

    # 이미지 유무 판단
    if item.thumb is None:
        Contents(title=item.title, content=item.content, blogger=item.blogger).create(session, auto_commit=True)
        responses = {200: {"status": "success", "detail": "No Thumb"}}
    else:
        Contents(title=item.title, content=item.content, blogger=item.blogger, thumb=item.thumb).create(session,
                                                                                                        auto_commit=True)
        responses = {200: {"status": "success", "detail": "Thumb"}}
    return responses
