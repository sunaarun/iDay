import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_secret.json")
firebase_admin.initialize_app(cred)

# create a db client
db = firestore.client()

# create some data to insert into db
data = {
    "student_name": "Dang Nguyen",
    "student_email": "haidangnng@gmail.com",
    "student_team": "Null",
}


def read_documents():
    docs = db.collection("Teams").stream()
    res = []
    for doc in docs:
        print(f"{doc.id} => {doc.to_dict()}")
        res.append(doc.to_dict())
    return res


# a function that add a document to our db
def add_doc(data):
    doc_ref = db.collection("Teams").document()
    doc_ref.set(data)
    print(doc_ref)

add_doc(data)

def delete_doc(id, collection_name):
    id = db.collection(collection_name).document(id).get()
    if id.exists:
        id.reference.delete()
        print("Deleted doc")
    else:
        print("No such Document")


# update a document
def update_doc(id, data, collection_name):
    # Get a reference to the document
    doc_ref = db.collection(collection_name).document(id)
    if doc_ref.get().exists:
        doc_ref.update(data)
        print("Document Updated")
    else:    
        print("No such Document")


read_documents()
d= {
    "student_name": " 3355Bilal",
    "student_email": "hassan@gmail.com",    
    "student_team": "Null",
}
doc = db.collection('Teams').document("1x2DG36yNa1mwbA3Q7y9")
id=doc.get()
update_doc(id.id, d, "Teams")