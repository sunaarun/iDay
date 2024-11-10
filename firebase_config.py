import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

# create a db client
db= firestore.client()

# create some data to insert into db
data={
    'student-name':'Sanaa Al-hdal',
    'student-email':'sanaalhdal@hotmail.com',
    'student-team':'Null'
}

async def read_documents():
    docs = await db.collection(u'Teams').document().get()
    print(docs.to_dict())
    return docs


# a function that add a document to our db
def add_doc(data, collection_name):
    doc_ref = db.collection(collection_name).document()
    doc_ref.set(data)
    print(doc_ref)


def delete_doc(id,collection_name):
    id= db.collection(collection_name).document(id).get()
    if id.exists:
        id.reference.delete()
        print('Deleted doc')
    else:
        print("No such Document")


# update a document
def update_doc(id, data, collection_name):
    doc_ref = db.collection(collection_name).document()
    doc_ref.update({'_id': id}, {'$set': data})