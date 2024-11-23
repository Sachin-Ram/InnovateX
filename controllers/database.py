import os
from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv
load_dotenv()

class database:

    @staticmethod
    def getConnection():

        try:
            connection=MongoClient("mongodb+srv://sachintheking25:{}@travelbot.jh79s.mongodb.net/?retryWrites=true&w=majority&appName=TravelBot".format(os.getenv('mongo_password')))  #get db connection

            #get the db and the collection
            db = connection["TravelBot"]         
            collection = db["authentication"]
            print(collection)
            return collection
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
