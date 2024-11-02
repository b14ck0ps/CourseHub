from fastapi import FastAPI

from api import courses, section, user

app = FastAPI()

app.include_router(user.router)
app.include_router(section.router)
app.include_router(courses.router)
