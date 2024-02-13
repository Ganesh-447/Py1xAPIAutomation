# Common headers

def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers


def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers

def common_headers_for_token_put_update():
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM="
    }
    return headers

