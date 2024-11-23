from controllers.database import database

def func():

    conn=database.getConnection()

    new_document = {
            "name": "John Doe",
            "email":"john.doe@example.com"
        }

        # Insert the document into the collection
    result = conn.insert_one(new_document)

    all_documents = conn.find()

    if not all_documents:
        print("No documents found in the collection.")
        return
    else:
        print("some are there")

    doc = list(all_documents)

        # Debugging: print the list of documents to see if it's empty
    print(f"Documents list: {doc}")  # Check the content of the list

        # Print each document in the collection
    for i in doc:
        print(i)

if __name__ == '__main__':

    func()