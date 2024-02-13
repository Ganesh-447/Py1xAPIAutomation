import json
import os
import pytest
from src.helpers.api_requests_wrapper import post_request
from src.constants.api_constants import API_Constants
from src.helpers.payload_manager import create_booking_payload, create_token_payload
from src.helpers.utils import common_headers_json
from src.helpers.common_verifications import verify_http_status_code, verify_json_key_not_null
from jsonschema import validate
from jsonschema.exceptions import ValidationError


class TestCreateBooking():

    def load_schema(self, schema_file):
        with open(schema_file, 'r') as file:
            return json.load(file)

    @pytest.mark.positive
    def test_postrequest_jsonschema_validation(self):
        response = post_request(url=API_Constants.url_create_booking(), auth=None, header=common_headers_json(),
                                payload=create_booking_payload(), in_json=False)
        bookingid = response.json()['bookingid']
        print(f'your booking id is {bookingid}')
        verify_http_status_code(response, 200)
        verify_json_key_not_null(bookingid)
        response_json = response.json()
        file = os.getcwd() + "/schema.json"
        schema = self.load_schema(file)
        #schema = self.load_schema("/Users/Ganesh/Py1xAPIAutomation/tests/jsonschema/schema.json")
        try:
            validate(instance=response_json, schema=schema)
        except ValidationError as e:
            print(e.message)
