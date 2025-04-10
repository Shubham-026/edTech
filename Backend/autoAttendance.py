import psycopg2
import pandas
import requests
from fastapi import FastAPI, Request
import time

app = FastAPI()

# PostgreSQL connection setup
conn = psycopg2.connect(
    host="localhost",
    database="first",
    user="postgres",
    password="123456"
)
cur = conn.cursor()

timeNow = time.strftime("%Y-%m-%d")

# Attendance System
class AttendanceSystem: 
    command1 = f'ALTER TABLE attendance ADD COLUMN "{timeNow}" TEXT DEFAULT \'absent\''
    cur.execute(command1)
    conn.commit()
    
    @staticmethod
    @app.post("/receive")
    async def attendance_receiver(request: Request):
        data = await request.json()
        student_id = data.get("id")
        time = data.get("time")
        # Store in DB
        query = f'UPDATE attendance SET "{timeNow}" = %s WHERE admin = %s'
        cur.execute(query, (time, student_id))
        conn.commit()
        print(f"Received attendance for ID: {student_id} at {time}")
        return {"status": "ok", "received_id": student_id, "received_time": time}


# TO RUN ---> "python -m uvicorn main:app --reload --port 8000"