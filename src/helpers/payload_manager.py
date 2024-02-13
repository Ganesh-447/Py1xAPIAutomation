from faker import Faker
import json

faker = Faker()

def create_booking_payload():
    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload
def create_booking_payload_dynamic():
    payload = {
        "firstname": faker.first_name(),
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload
def create_booking_put_payload():
    payload = {
        "firstname": "Ganesh",
        "lastname": "Grandhi",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    return payload

def create_token_payload():
    payload = {
        "username": "admin",
        "password": "password123"
    }
    return payload
