from controllers.database import Database

class auth:

    def __init__(self,name,email):

        self.name=name

        self.email=email

        self.conn=Database.getConnection()

    def authenticate(self):

        user=self.conn.find_one({"email":self.email})

        print(user)

        if user :

            return True
        
        else :

            return False
    
    def adduser(self):

        mail=self.email

        name=self.name

        data={

            "name":name,
            "email":mail
        }

        result=self.conn.insert_one(data)

        print("Inserted document ID:", result.inserted_id)

    def add_data(self,data):

        name=self.name
        mail=self.email

        conn=self.conn
        
        collection = conn["search_log"]

        data_to_insert = {
            "name": name,
            "email": mail,
            "search_data": data
        }

        insert_result = collection.insert_one(data_to_insert)

        print(f"Data inserted with document ID: {insert_result.inserted_id}")

        return "success"





