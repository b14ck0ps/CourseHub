from typing import List, Optional

import fastapi
from fastapi import HTTPException
from pydantic import BaseModel

router = fastapi.APIRouter()
sections = []


class Section(BaseModel):
    id: int
    title: str
    description: Optional[str] = None


@router.post("/sections/", response_model=Section)
def create_section(section: Section):
    sections.append(section)
    return section


@router.get("/sections/", response_model=List[Section])
def read_sections():
    return sections


@router.get("/sections/{section_id}", response_model=Section)
def read_section(section_id: int):
    for section in sections:
        if section.id == section_id:
            return section
    raise HTTPException(status_code=404, detail="Section not found")


@router.put("/sections/{section_id}", response_model=Section)
def update_section(section_id: int, updated_section: Section):
    for index, section in enumerate(sections):
        if section.id == section_id:
            sections[index] = updated_section
            return updated_section
    raise HTTPException(status_code=404, detail="Section not found")


@router.delete("/sections/{section_id}", response_model=Section)
def delete_section(section_id: int):
    for index, section in enumerate(sections):
        if section.id == section_id:
            deleted_section = sections.pop(index)
            return deleted_section
    raise HTTPException(status_code=404, detail="Section not found")


app = fastapi.FastAPI()
app.include_router(router)
