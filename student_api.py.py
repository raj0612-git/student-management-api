from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student (BaseModel):
  rollNo: int
  name: str
  age: int
  course: str
  email: str
  
students_db = []

@app.get("/")
def read_root():
  return {"message": "Welcome to Students Database"}
  
@app.get("/students/")
def see_studentData():
    return students_db
  
@app.post("/studernts/")
def create_studentData(student: Student):
  students_db.append(student)
  return {"message": "Student data created successfully", "student": studernt}
  
@app.get("/student/")
def see_studentData(rollNo: int):
  for student in students_db:
    if student.rollNo == rollNo:
      return {"student": student}
  return {"error": "Student data not found"}

@app.put("/students/")
def update_studentData(rollNo: int, update_student = Student):
  for index, student in enumerate(students_db):
    if student.rollNo == rollNo:
      students_db[index] = update_student
      return {"message": "Student data updated successfully", "student": updated_student}
  return {"error": "Student data not found"}

@app.delete("/student/")
def delete_studentData(rollNo: int):
  for index, student in enumerate(students_db):
    if student.rollNo == rollNo:
      deleted_student = students_db.pop(index)
      return {"message": "Student data deleted successfully", "student": deleted_student}
  return {"error": "Student data not found"}