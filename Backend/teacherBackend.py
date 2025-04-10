# teacher.py
from fastapi import APIRouter

teacher_router = APIRouter(prefix="/teacher", tags=["Teacher"])

@teacher_router.get("/announcements")
def teacher_announcements():
    return {"data": "Post or view announcements"}

@teacher_router.get("/homework")
def manage_homework():
    return {"data": "Add or manage homework"}

@teacher_router.get("/attendance")
def mark_attendance():
    return {"data": "Mark attendance"}

@teacher_router.get("/profile")
def teacher_profile():
    return {"name": "Mr. Kumar", "subject": "Maths"}

