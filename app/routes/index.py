from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy import MetaData
from sqlalchemy.orm import Session
from starlette.responses import Response

from app.database.conn import db, Base
from app.database.schema import Contents

router = APIRouter()


@router.get("/")
async def index(session: Session = Depends(db.session),):
    """
    :param session:
    :return:
    """

    # 테이블 생성 명령어
    Base.metadata.create_all(db.engine)

    # Contents(title="title", content="asdasd<br><br>  4<br>  3 <br>2<br>1", ).create(session, auto_commit=True)

    first_one = session.query(Contents).first()
    print(first_one.title)

    for row in session.query(Contents).all():
        print(row.title)
        print("이거보시라")

    first_one.title = "title2"
    Contents.update(first_one, session, auto_commit=True)

    current_time = datetime.utcnow()

    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')}")