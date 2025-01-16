import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from models import Student, Group, StudentGroup, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from settings import get_database_url
from student import student_api,group_api
DATABASE_CONFIG = {
    'dialect': 'mysql+pymysql',
    'username': 'root',
    'password': 'HYW',
    'host': '127.0.0.1',
    'port': '3306',
    'database': 'houyanwu',
}

DATABASE_URL = get_database_url(DATABASE_CONFIG)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI()

# 创建数据库会话依赖
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
app = FastAPI()

app.include_router(student_api, prefix="/students")
app.include_router(group_api, prefix="/groups", tags=["groups"])

if __name__ == '__main__':
    uvicorn.run('main:app', host='127.0.0.1', port=8000, reload=True,
               workers=1)
