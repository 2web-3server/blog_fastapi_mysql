from datetime import datetime

from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.schema import Contents, Comments, Category

router = APIRouter(
    prefix="/category",
    tags=["category"],
    responses={404: {"description": "Not found"}},
)


# All List
@router.get("/{blogger}")
async def get_category(blogger: str, session: Session = Depends(db.session), ):
    # 글 전체목록 불러오기
    results = session.query(Category).filter(Category.blogger == blogger).all()
    return results


class Category_name(BaseModel):
    category: str


# All list in category
@router.post("/{blogger}")
async def contents_from_category(item: Category_name, blogger: str, session: Session = Depends(db.session)):
    results = Category(name=item.category, blogger=blogger).create(session, auto_commit=True)

    return results