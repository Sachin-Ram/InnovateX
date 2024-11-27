from flask import Flask,Blueprint,request
from services.expensesplitter import expensesplitter

expensesplit_ep=Blueprint("expense",__name__)

@expensesplit_ep.route("/split",methods=['GET','POST'])

def func():

    req=request.get_json()
    amount=req['session']['amount']['value']

    expense_obj = expensesplitter(amount)

    data=expense_obj.split()

    return data