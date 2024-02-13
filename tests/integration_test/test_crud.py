import pytest
from src.helpers.api_requests_wrapper import post_request, put_request,delete_request
from src.constants.api_constants import API_Constants
from src.helpers.payload_manager import create_booking_payload, create_token_payload,create_booking_put_payload
from src.helpers.utils import common_headers_json,common_headers_for_token_put_update
from src.helpers.common_verifications import verify_http_status_code, verify_json_key_not_null


class TestCrud(object):

    @pytest.fixture()
    def createtoken_tc1(self):
        response = post_request(url=API_Constants.url_create_token(), auth=None, header=common_headers_json(),
                                payload=create_token_payload(), in_json=False)
        token = response.json()["token"]
        print(token)
        verify_http_status_code(response, 200)
        verify_json_key_not_null(token)
        return token
    @pytest.fixture()
    def postrequest_tc2(self):
        response = post_request(url=API_Constants.url_create_booking(), auth=None, header=common_headers_json(),
                                payload=create_booking_payload(), in_json=False)
        bookingid = response.json()['bookingid']
        print(f'your booking id is {bookingid} and your details are{response.json()}')
        verify_http_status_code(response, 200)
        verify_json_key_not_null(bookingid)
        return bookingid

    #bookingid, token
    def test_putrequest_tc3(self,postrequest_tc2):
        booking_id = str(postrequest_tc2)
        put_url = API_Constants.url_create_booking()+ "/"+booking_id
        response = put_request(url =put_url,auth=None,header=common_headers_for_token_put_update(),
                               payload= create_booking_put_payload(), in_json= False)
        print(f' your updated details are {response.json()}')
        verify_http_status_code(response,200)

    def test_deleterequest_tc4(self):
        delete_url = API_Constants.url_create_booking()+ "/3922"
        response = delete_request(url=delete_url,auth=None,header=common_headers_for_token_put_update()
                                  , in_json= False)
        print(response.json())
        verify_http_status_code(response,201)
