import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

routeMap = {
    "0.0.0.0:8000": "postgresql://postgres:5798@localhost/db1",
    "localhost:8000": "postgresql://postgres:5798@localhost/db2",
    }


# extends BaseHTTPMiddleware filter your router name and set database_url in your envioment.
class DatabaseSelector(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        host = request.headers["host"]
        print("request.headers: ", request.headers["host"])
        # url_param = str(request.url).split("/")
        # if "api" in str(request.url):
        #     url_param.remove("api")
        # route_name = url_param[3]
        # if route_name not in list(routeMap.keys()):
        #     SQLALCHEMY_DATABASE_URL = routeMap["default"]
        # else:
        #     SQLALCHEMY_DATABASE_URL = routeMap[route_name]
        SQLALCHEMY_DATABASE_URL = routeMap[host]
        os.environ["SQLALCHEMY_DATABASE_URL"] = SQLALCHEMY_DATABASE_URL
        response = await call_next(request)
        return response


def get_db():
    # SQLALCHEMY_DATABASE_URL = "postgresql://postgres:5798@localhost/db1"
    SQLALCHEMY_DATABASE_URL = os.getenv('SQLALCHEMY_DATABASE_URL')
    print("SQLALCHEMY_DATABASE_URL: ", SQLALCHEMY_DATABASE_URL)

    engine = create_engine(
        SQLALCHEMY_DATABASE_URL
    )
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
