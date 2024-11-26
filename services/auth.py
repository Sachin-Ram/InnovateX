from controllers.database import database

class auth:

    def __init__(self,name,email):

        self.name=name

        self.email=email

        self.conn=database.getConnection()

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



