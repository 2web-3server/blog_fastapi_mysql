from dataclasses import asdict

import uvicorn
from fastapi import FastAPI

from app.database.conn import db
from app.common.config import conf
from app.routes import index


def create_app():
    """
    앱 함수 실행
    :return:
    """
    c = conf()
    app = FastAPI()
    conf_dict = asdict(c)
    db.init_app(app, **conf_dict)

    # 라우터 정의
    app.include_router(index.router)

    return app


app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)