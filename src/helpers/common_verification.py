#Common verification function
#Status code
#headers
#data verification
#json schema


def verify_status_code(response_data, expected_data):
    assert response_data.status_code == expected_data, "Failed status code match"

#key can be any data which we want to verify here booking_id/checkin date, in other api different value
def verify_response_key(key,expected_data):
    assert key == expected_data

def verify_json_key_not_null(key):
    assert key!=0, "Failed - key is non empty" +key
    assert key >= 0, "Failed - key is greater than zero"

#in this case key is token
def verify_for_token_not_null(key):
    assert key!=0, "Failed - key is non empty" +key




