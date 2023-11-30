from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DATABASE

class Dojo:
    def __init__(self, data_dict):
        self.id = data_dict["id"]
        self.name = data_dict["name"]
        self.dojo_location = data_dict["dojo_location"]
        self.favourite = data_dict["favourite"]
        self.comments = data_dict["comments"]
        self.created_at = data_dict["created_at"]
        self.updated_at = data_dict["updated_at"]

    #  Queries  = classmethods
    @classmethod
    def create(cls, data):
        query = """
                INSERT INTO dojos
                            (name, dojo_location, favourite, comments)
                       VALUES 
                            (%(name)s, %(dojo_location)s,%(favourite)s, %(comments)s );"""
        # - INSERT STATEMENT RETURNS THE NEW INSERTED ROW ID
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("INSERT STATEMENT RETURN  : ", db_result, "*" * 25)
        return db_result

    @classmethod
    def get_one_by_id(cls, data):
        query = """ SELECT * FROM dojos WHERE id=%(id)s; """
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥", db_result, "🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        user = cls(db_result[0])
        return user

    @classmethod
    def get_one_by_email(cls, data):
        query = """ SELECT * FROM dojos WHERE email=%(email)s; """
        db_result = connectToMySQL(DATABASE).query_db(query, data)
        print("🔥🔥🔥🔥🔥🔥🔥🔥🔥", db_result, "🔥🔥🔥🔥🔥🔥🔥🔥🔥")
        if db_result:
            return cls(db_result[0])
        return False

    @staticmethod
    def validate(data):
        is_valid = True
        if len(data["first_name"]) < 2:
            flash("First name too short.")
            is_valid = False
        if len(data["last_name"]) < 2:
            flash("Last name too short.")
            is_valid = False
        #  Email Validation
        if not EMAIL_REGEX.match(data["email"]):
            flash("Email is not valid.")
            is_valid = False
        # Password Validation
        # validate length
        if len(data["password"]) < 8:
            flash("Password must be 8.")
            is_valid = False
            # validate if pw and confirm_pw match
        elif data["password"] != data["confirm_password"]:
            flash("Passwords must match.")
            is_valid = False
        return is_valid