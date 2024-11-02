from typing import List

import fastapi
from fastapi import HTTPException
from pydantic import BaseModel

router = fastapi.APIRouter()

courses = []


class Course(BaseModel):
    id: int
    title: str
    description: str


@router.post("/courses/", response_model=Course)
def create_course(course: Course):
    courses.append(course)
    return course


@router.get("/courses/", response_model=List[Course])
def read_courses():
    return courses


@router.get("/courses/{course_id}", response_model=Course)
def read_course(course_id: int):
    for course in courses:
        if course.id == course_id:
            return course
    raise HTTPException(status_code=404, detail="Course not found")


@router.put("/courses/{course_id}", response_model=Course)
def update_course(course_id: int, updated_course: Course):
    for index, course in enumerate(courses):
        if course.id == course_id:
            courses[index] = updated_course
            return updated_course
    raise HTTPException(status_code=404, detail="Course not found")


@router.delete("/courses/{course_id}", response_model=Course)
def delete_course(course_id: int):
    for index, course in enumerate(courses):
        if course.id == course_id:
            deleted_course = courses.pop(index)
            return deleted_course
    raise HTTPException(status_code=404, detail="Course not found")


app = fastapi.FastAPI()
app.include_router(router)
