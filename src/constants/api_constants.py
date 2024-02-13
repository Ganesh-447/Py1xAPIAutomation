# Add constants here

# 1st way create by using constant.

url = "https://restful-booker.herokuapp.com/booking/"


# 2nd way creating by using functions.

def base_url():
    return "https://restful-booker.herokuapp.com"


def url_create_booking():
    return "https://restful-booker.herokuapp.com/booking"


def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"


# Update - Patch, Put , Delete - Booking id

def url_patch_put_delete_booking(booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str(booking_id)


# 3rd way using Class

class API_Constants():

    @staticmethod
    def base_url():
        return "https://restful-booker.herokuapp.com"

    @staticmethod
    def url_create_booking():
        return "https://restful-booker.herokuapp.com/booking"

    @staticmethod
    def url_create_token():
        return "https://restful-booker.herokuapp.com/auth"

    def url_patch_put_delete_booking(self, booking_id):
        return "https://restful-booker.herokuapp.com/booking/" + str(self, booking_id)
