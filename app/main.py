from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from app.database.database import cursor
from app.database.database import connection

app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def add_student_page(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="add_student.html",
        context={}
    )


@app.post("/students")
async def create_student(
    student_id: int = Form(...),
    first_name: str = Form(...),
    last_name: str = Form(...),
    date_of_birth: str = Form(...),
    class_name: str = Form(...)
):
    cursor.execute(
        """
        INSERT INTO students
        VALUES (?, ?, ?, ?, ?)
        """,
        (
            student_id,
            first_name,
            last_name,
            date_of_birth,
            class_name
        )
    )

    connection.commit()

    return RedirectResponse(
        url="/students",
        status_code=303
    )


@app.get("/students", response_class=HTMLResponse)
async def get_students(request: Request):

    cursor.execute(
        """
        SELECT *
        FROM students
        """
    )

    rows = cursor.fetchall()

    students = []

    for row in rows:
        students.append(
            {
                "student_id": row[0],
                "first_name": row[1],
                "last_name": row[2],
                "date_of_birth": row[3],
                "class_name": row[4]
            }
        )

    return templates.TemplateResponse(
        request=request,
        name="students.html",
        context={"students": students}
    )