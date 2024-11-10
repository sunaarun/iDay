from typing import Union

from fastapi import FastAPI

from firebase_config import add_doc, read_documents

app = FastAPI()




@app.get("/documents")
def read_data():
    data = read_documents()
    return data


# data = {
#     "student-name": "Dang Nguyen",
#     "student-email": "haidangnng@gmail.com",
#     "student-team": "Null",
# }


@app.post("/documents")
def create_document(name, email, team):
    data = add_doc(
        {
            "student_team": team,
            "student_email": email,
            "student_name": name,
        }
    )
    return data


# @app.post('/document')
# def create_item(data):
#     add_doc(data)
