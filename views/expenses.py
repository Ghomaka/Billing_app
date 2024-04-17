from flask import Blueprint, request, Response

from controllers.expenses import *
from models.exceptions import ModelNotFoundError

expenses_view = Blueprint('expenses', __name__, url_prefix='/expexpenses')

@expenses_view.route('/', methods=['GET', 'POST'])
def list_or_create():
    if request.method == 'GET':
        return get_all_expenses()
    else:
        
        data = request.get_json()

        return Response(save_expense(data['name'],data['amount'],data['description'],data['cat_id'],data['user_id']), status=201)

@expenses_view.route('/<id>', methods=['GET', 'PATCH', 'DELETE'])
def get_or_update_or_delete_instance(id):
    if request.method == 'GET':
        try:
            return get_expense_with_id(id)
        except ModelNotFoundError:
            return Response("<h1>Instance not found</h1>", status=404)
    elif request.method == 'PATCH':
        data = request.get_json()
        return Response(save_expense(name=data['name'],email=data['email'],password=data['password']), status=201)
    elif request.method == 'DELETE':
        return Response(delete_expense(id), status=201)

