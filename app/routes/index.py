from datetime import datetime
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import Response
from app.database.conn import db, Base

router = APIRouter()

@router.get("/refresh")
async def index(session: Session = Depends(db.session),):
    """
    :param session:
    :return:
    """
    # 테이블 생성 명령어
    Base.metadata.create_all(db.engine)

    current_time = datetime.utcnow()

    return Response(f"Notification API (UTC: {current_time.strftime('%Y.%m.%d %H:%M:%S')}")