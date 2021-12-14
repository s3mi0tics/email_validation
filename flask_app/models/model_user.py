import re 
from flask import flash
from flask_app.config.mysqlconnection import connectToMySQL
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$') 

DATABASE = 'email_validation_db'
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.email = data['email']
    
    @staticmethod
    def validate_email ( user ):
        is_valid = True
        all_users = User.get_all()
        if not EMAIL_REGEX.match(user['email']):
            flash("Email invalid")
            is_valid = False
        for user1 in  all_users: 
            if user1.email == user['email']:
                flash("email in use")
                is_valid = False
        return is_valid
    
    @classmethod
    def create(cls, data:dict) ->int:
        query = "INSERT INTO emails (email) VALUES (%(email)s);"
        return connectToMySQL(DATABASE).query_db(query, data)
    
    @classmethod
    def get_all(cls) ->int:
        query = "SELECT * FROM emails;"
        results = connectToMySQL(DATABASE).query_db(query)
        if results:
            all_users = []
            for user in results:
                all_users.append(cls(user))
            return all_users
        return False