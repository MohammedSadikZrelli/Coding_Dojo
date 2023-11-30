from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE
import re  # the regex module




class User:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.first_name = data_dict["first_name"]
        self.last_name = data_dict["last_name"]
        self.email = data_dict["email"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    #  Queries  = classmethods

    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO users 
                            (first_name, last_name, email)
                       VALUES 
                            (%(first_name)s, %(last_name)s,%(email)s);"""
        # - INSERT STATEMENT RETURNS THE NEW INSERTED ROW ID
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("INSERT STATEMENT RETURN  : ", db_result, "*" * 25)
        return db_result

    @classmethod
    def get_one_by_id(cls, data):
        query = """ SELECT * FROM users WHERE id=%(id)s; """
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥", db_result, "🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        user = cls(db_result[0])
        return user

    @classmethod
    def get_one_by_email(cls, data):
        query = """ SELECT * FROM users WHERE email=%(email)s; """
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥", db_result, "🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        if db_result:
            print("--------------------",db_result[0])
            return db_result[0]
        else: return False

