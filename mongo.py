from pymongo import MongoClient
client = MongoClient('mongodb+srv://vtsljogi009:vatsal123@cluster0.mimsx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')
db=client['user']
collection=db['users']

document={'name':'vatsal','email':'vatsal@gmail.com','password':'1234'}

inseret=collection.insert_one(document)

print('Document inserted with id:', inseret.inserted_id)
# client.commit()
client.close()