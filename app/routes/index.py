from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db, Base
from app.database.schema import Contents, Category, Comments

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    :param session:
    :return:
    """

    # 테이블 생성 명령어
    Base.metadata.create_all(db.engine)

    # Contents(category_id=1, title="연습이야", content="asdasd<br><br>  4<br>  3 <br>2<br>1", ).create(session, auto_commit=True)

    Comments(content_id=2, email="tjrgh@kakao.com", password="임시비번", content="댓글내용").create(session, auto_commit=True)

    # first_one = session.query(Contents).filter(Contents.title == "연습이야")
    # for row in first_one:
    #     print(row)

    # for row in session.query(Contents).all():
    #     print(row.title)
    #     print("이거보시라")
    #
    # first_one.title = "title2"
    # Contents.update(first_one, session, auto_commit=True)
    # Contents.delete(first_one, session, auto_commit=True)
    current_time = datetime.utcnow()

    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')}")