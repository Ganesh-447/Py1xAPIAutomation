# read the csv or Excel file
# create a function create token which can take values from Excel file
# verify the expected result.

# read the Excel - openpyxl

import openpyxl
import requests
import pytest
from src.constants.api_constants import API_Constants
from src.helpers.utils import common_headers_json
from src.helpers.common_verifications import verify_http_status_code


# step-1 read the file and put content in []

def read_credentials_from_excel(file_path):
    credentials = []
    workbook = openpyxl.load_workbook(file_path)
    sheet = workbook.active
    for row in sheet.iter_rows(min_row=2, values_only=True):
        username, password = row
        credentials.append({"username": username, "password": password})
    print(credentials)
    return credentials


def make_request_auth(username, password):
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(url=API_Constants.url_create_token(), headers=common_headers_json(),
                             json=payload)
    # verify_http_status_code(response, 200)
    #print(response.json())
    return response


def test_post_create_token():
    file_path = "testdata1_ddt.xlsx"
    credentials = read_credentials_from_excel(file_path)
    for user_cred in credentials:
        username = user_cred["username"]
        password = user_cred["password"]
        print(username, password)
        response = make_request_auth(username, password)
        print(response)
        print(response.json)

    # Make req auth -> Run this function for the rows in Excel
