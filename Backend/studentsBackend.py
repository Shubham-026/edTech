# student.py
from fastapi import APIRouter

student_router = APIRouter(prefix="/student", tags=["Student"])

@student_router.get("/announcements")
def get_announcements():
    return {"data": "Announcements for students"}

@student_router.get("/homework")
def get_homework():
    return {"data": "Homework for student"}

@student_router.get("/attendance")
def view_attendance():
    return {"data": "Attendance data"}

@student_router.get("/profile")
def student_profile():
    return {"name": "Shubham", "class": 12, "roll": 21}