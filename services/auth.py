from controllers.database import database

class auth:

    def __init__(self,name,email):

        self.name=name

        self.email=email

    def authenticate(self):

        conn=database.getConnection()

        user=conn.find_one({"email":self.email})

        print(user)

        if user :

            return True
        
        return False