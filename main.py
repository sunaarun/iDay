from typing import Union

from fastapi import FastAPI

from firebase_config import add_doc, delete_doc, read_documents, read_one_doc, update_doc

app = FastAPI()




@app.get("/documents")
def read_data():
    data = read_documents()
    return data

# return a single document
@app.get("/documents/{document_id}")
def read_document(document_id: str):
    data = read_one_doc(document_id, "Teams")
    return data


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

@app.put("/documents/{document_id}")
def update_document(document_id: str, name, email, team):
    data = update_doc(document_id, data=
        {
            "student_team": team,
            "student_email": email,
            "student_name": name,
        }, collection_name="Teams")
    return data

@app.delete("/documents/{document_id}")
def delete_document(document_id: str):
    data = delete_doc(document_id, "Teams")
    return data


