import firebase_admin
from firebase_admin import credentials, firestore

cred = credentials.Certificate("firebase_secret.json")
firebase_admin.initialize_app(cred)

# create a db client
db = firestore.client()

# create some data to insert into db
data = {
    "student-name": "Dang Nguyen",
    "student-email": "haidangnng@gmail.com",
    "student-team": "Null",
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


def delete_doc(id, collection_name):
    id = db.collection(collection_name).document(id).get()
    if id.exists:
        id.reference.delete()
        print("Deleted doc")
    else:
        print("No such Document")


# update a document
def update_doc(id, data, collection_name):
    doc_ref = db.collection(collection_name).document()
    doc_ref.update({"_id": id}, {"$set": data})


read_documents()

