from typing import Union

from fastapi import FastAPI

from firebase_config import add_doc, read_documents

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.get("/documents")
async  def read_data() :
    data= await read_documents()
    return data
    # if data.empty: return





# @app.post('/document')
# def create_item(data):
#     add_doc(data)
