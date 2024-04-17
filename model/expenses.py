
import os

from models.users import User
from models.categories import Category
from models.expenses import Expense

from werkzeug.utils import secure_filename

# from constants import UPLOAD_FOLDER

def get_all_expenses(return_objects=False):
    """
    Set return_objects to True if you want to return a 
    model instance instead of JSON
    """
    objects = Expense.read()

    if not return_objects:
        list_of_objects = [
            obj.toJSON() for obj in objects
        ]
        return list_of_objects
    
    return objects

def get_expense_with_id(id, return_object=False):
    """
    Set return_object to True if you want to return a 
    model instance instead of JSON
    """
    obj = Expense.read(id)

    return obj if return_object else obj.toJSON()

def save_expense(name, amount, description, category_id, id=None, user_id=None, return_object=False):
    if id != None:
        expense = get_expense_with_id(id, return_object=True)
        expense.name, expense.amount, expense.description, expense.category_id,expense.user_id = (
            name, amount, description, category_id,user_id
        )
    else:
        expense = Expense(
            name=name,amount=amount, 
            description=description, category=category_id, user=user_id
        )

    expense.save()

    return expense if return_object else expense.toJSON()
    
def delete_expense(id):
    expense = get_expense_with_id(id)
    expense.delete()

    return expense.toJSON()