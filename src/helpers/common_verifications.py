# HTTP Status Codes


def verify_http_status_code(response_data, expect_data):
    assert response_data.status_code == expect_data, 'Expected HTTP status is' + expect_data


def verify_json_key_not_null(key):
    assert key is not None, "key is non empty" + key
    #assert key > 0, "key is greater than 0"


def verify_response_time():
    pass

# status
# headers
# response body which is data verification
# json schema
