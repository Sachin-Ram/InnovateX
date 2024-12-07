from flask import Flask


class featured_plan_services:

    def __init__(self,hotel_obj,flight_obj):

        self.hotel_obj=hotel_obj

        self.flight_obj=flight_obj

    def calculate_amount(self,flightplan,hotelplan):

        flight_price=self.flight_obj.get('flightplan').get("price")

        hotel_price=self.hotel_obj.get('hotelplan').get("price")

        return flight_price+hotel_price