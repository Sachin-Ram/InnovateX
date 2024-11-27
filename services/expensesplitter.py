from flask import Flask,Blueprint,make_response,jsonify
class expensesplitter:

    def __init__(self,amount):

        self.amount=amount

    def split(self):

        food=0.4

        travel=0.3

        entertainment=0.2

        ShoppingSouvenirs= 0.05

        MiscellaneousExpenses= 0.05

        food_amount=food *self.amount
        travel_amount=travel*self.amount
        entertainment_amount=entertainment*self.amount
        ShoppingSouvenirs_amount=ShoppingSouvenirs*self.amount
        MiscellaneousExpenses_amount=MiscellaneousExpenses*self.amount

        data={
            "food":food_amount,
            "travel":travel_amount,
            "entertainment":entertainment_amount,
            "shopping":ShoppingSouvenirs_amount,
            "Miscellaneous":MiscellaneousExpenses_amount
        }

        return make_response(jsonify(data),200)

