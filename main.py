from fastapi import FastAPI

from api import courses, sections, users
from db.db_setup import engine
from db.models import course, user

user.Base.metadata.create_all(bind=engine)
course.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)
app.include_router(sections.router)
app.include_router(courses.router)
