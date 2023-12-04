from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DATABASE
from flask import flash
from flask_app.models import user_model

class Recipe:
    def __init__(self,data):
        self.id=data["id"]
        self.user_id=data["user_id"]
        self.name=data["name"]
        self.instructions=data["instructions"]
        self.date=data["date"]
        self.under=data["under"]
        self.description=data["description"]
        self.poster=user_model.User.get_by_id({'id':self.user_id})
        
    
    @classmethod
    def create(cls,data):
        query="""INSERT INTO recipes 
                            (user_id,name,instructions,date,under,description)
                            VALUES (%(user_id)s,%(name)s,%(instructions)s,%(date)s,%(under)s,%(description)s);"""
        return connectToMySQL(DATABASE).query_db(query,data)
    
    @classmethod
    def get_all(cls):
        query="""SELECT * FROM recipes;"""
        results=connectToMySQL(DATABASE).query_db(query)
        all_recipes=[]
        for row in results:
            all_recipes.append(cls(row))
        return all_recipes
    
    @classmethod
    def get_by_id(cls,data):
        query="""SELECT * FROM recipes WHERE id=%(id)s;"""
        result=connectToMySQL(DATABASE).query_db(query,data)
        if result:
            return cls(result[0])
        return None
    
    @classmethod
    def update(cls,data):
        print("🐝"*10, data,"🐝"*10)
        query=""" UPdate recipes SET name=%(name)s,instructions=%(instructions)s,date=%(date)s,
                under=%(under)s,description=%(description)s WHERE id=%(id)s; """
        return connectToMySQL(DATABASE).query_db(query,data)
    @classmethod
    def destroy(cls,data):
        query="""DELETE FROM recipes WHERE id=%(id)s;"""
        return connectToMySQL(DATABASE).query_db(query,data)
            
    @staticmethod
    def validate(data):
        is_valid=True
        if len(data['name'])<3:
            is_valid=False
            flash(" recipe name is required")
        if len(data['instructions'])<3:
            is_valid=False
            flash("recipe instructions is required")
        if len(data['description'])<3:
            is_valid=False
            flash("recipe description must be at least 10")
        if (data['date'])=="":
            is_valid=False
            flash("recipe date must be provided")
        return is_valid