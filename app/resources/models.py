from flask_restful import Resource
from flask import jsonify


# A list for holding book itesms
books = [
    {'id': 1, 'title': 'Python Programming'}, {'id': 3, 'title': 'Java programming'}

]
class Books(Resource):

    def get(self):
        return (books)
