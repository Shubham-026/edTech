import requests
import time


while True:


    print("enter the id")
    studentId = input()
    attendanceTime = time.strftime("%H:%M:%S")

    url = "http://localhost:8000/receive"
    
    # THE UPLOAD CODE HERE
    response = requests.post(
        url,
        json={
            "id": studentId,
            "time": attendanceTime
        }
    )


    data = response.json()
    print("Server Response:", data)

    print("Attendance of ",studentId," recorded at Time " , attendanceTime)
