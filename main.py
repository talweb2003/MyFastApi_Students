from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI() 
from fastapi.middleware.cors import CORSMiddleware
app.add_middleware(
 CORSMiddleware,
 allow_origins=["*"],
 allow_credentials=True,
 allow_methods=["*"],
 allow_headers=["*"],
)
class student(BaseModel):
    id:int
    name:str
    grade:int
students=[
    student(id=1,name="ALI",grade=5),
    student(id=2,name="AMARA",grade=7),
    student(id=3,name="Hocine",grade=3)
]
@app.get("/students/")
def get_students():
    return students
@app.post("/students/")
def create_new_student(new_student:student):
    students.append(new_student)
    return new_student
@app.put("/students/{student_id}")
def Update_student(student_id:int,updated_student:student):
    for index,student in enumerate(students):
        if student.id==student_id:
            students[index]=updated_student
            return updated_student
    return{"error":"student not found"}
@app.delete("/students/{student_id}")
def delete_student(student_id:int):
    for index,student in enumerate(students):
        if student.id==student_id:
          del students[index]
          return {"message":"student deleted"}
    return{"error":"student not found"}