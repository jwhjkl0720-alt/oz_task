# from flask_smorest import Blueprint, abort
from flask_restful import Resource, request
from schemas import BookSchema

# blq = Blueprint('books', 'books', url_prefix='/books', description='Operations on books')

books = []
book_schema = BookSchema()
books_schema = BookSchema(many=True)

class Book(Resource):
    def get(self, name):
        for book in books:
            if book['name'] == name:
                return book
        return {'msg':'Book not found'}, 404 # msg, code
        
    def post(self, name):
        for book in books:
            if book['name'] == name:
                return{'msg':'Book Already exists'}, 400
        data = request.get_json()

        new_book = {'name': name, 'price': data['price']}
        books.append(new_book)

        return new_book
    
    def put(self, name):
        data = request.get_json()
        if not data or 'price' not in data:
            return {'msg': 'price is required'}, 400

        for book in books:
            if book['name'] == name:
                book['price'] = data['price']
                return book
    
        # 만약, 업데이트하고자하는 책 데이터가 없다면 -> 추가한다
        new_book = {'name': name, 'price': data['price']}
        books.append(new_book)
        return new_book
    
    def delete(self, name):
        global books
        books = [book for book in books if book['name'] != name]
        return {'msg':'Book Deleted'}