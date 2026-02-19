from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel

app = FastAPI()

students = {
    1:{
        "Name":"Adhrit",
        "Class":11,
        "Skill":"Greatest Programmer"
    },
    2:{
        "Name":"Luffy",
        "Class":1,
        "Skill":"Greatest Pirate"
    },
    3:{
        "Name":"Robin",
        "Class":111,
        "Skill":"Genius in Histry"
    }

}

class Student(BaseModel):
    Name:str
    Class:int
    Skill:str
    
@app.get("/students/{student_id}")
def students_data(student_id:int = Path(..., gt=0, description="Please Enter the id")):
    if student_id not in students:
        raise HTTPException(status_code=404, detail="You entered the wrong id")
    else:
        return students[student_id]

@app.get("/students")
def student_name(name:str):
    for student_id in students:
        if students[student_id]["Name"] == name:
            return students[student_id]
        
        raise HTTPException(status_code=404, detail="You entered the wrong id")
    
@app.post("/add/{student_id}")
def add_student(student_id:int, student:Student):
    if student_id in students:
        raise HTTPException(status_code=409, detail="Its already stored")
    students[student_id] = student
    return students[student_id]
