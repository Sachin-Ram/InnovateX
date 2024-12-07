import os
from flask import Flask
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from dotenv import load_dotenv

load_dotenv()

class Database:

    @staticmethod
    def getConnection():
        try:
            # Connect to MongoDB Atlas using the password from environment variables
            connection = MongoClient(
                "mongodb+srv://sachintheking25:{}@travelbot.jh79s.mongodb.net/?retryWrites=true&w=majority&appName=TravelBot".format(
                    os.getenv('mongo_password')
                )
            )  # Get db connection

            # Get the db object
            db = connection["TravelBot"]
            
            print(f"Connected to database: {db.name}")  # This prints the name of the connected database

            return db  # Return the database object instead of the collection
        
        except Exception as e:
            print(f"Unexpected error: {e}")
            raise
