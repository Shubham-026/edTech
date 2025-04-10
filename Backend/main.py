# main.py
from fastapi import FastAPI
from student import student_router
from teacher import teacher_router
import time
import os


app = FastAPI()

# include routers
app.include_router(student_router)
app.include_router(teacher_router)

@app.get("/")
def root():
    return {"msg": "EdTech API running..."}
