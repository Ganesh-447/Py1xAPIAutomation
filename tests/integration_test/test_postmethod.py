import pytest
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import API_Constants
from src.helpers.payload_manager import create_booking_payload,create_token_payload
from src.helpers.utils import common_headers_json
from src.helpers.common_verifications import verify_http_status_code, verify_json_key_not_null


class TestCreateBooking():

    @pytest.mark.positive
    def test_postrequest_tc1(self):
        response = post_request(url=API_Constants.url_create_booking(), auth=None, header=common_headers_json(),
                                payload=create_booking_payload(), in_json=False)
        bookingid = response.json()['bookingid']
        print(f'your booking id is {bookingid}')
        verify_http_status_code(response, 200)
        verify_json_key_not_null(bookingid)

    @pytest.mark.negative
    def test_postrequest_tc2(self):
        response = post_request(url=API_Constants.url_create_booking(), auth=None, header=common_headers_json(),
                                payload={}, in_json=False)

        verify_http_status_code(response, 500)


    @pytest.mark.positive
    def test_createtoken_tc2(self):
         response = post_request(url=API_Constants.url_create_token(), auth=None, header=common_headers_json(),
                            payload=create_token_payload(), in_json=False)
         print(response.json())
         verify_http_status_code(response, 200)









