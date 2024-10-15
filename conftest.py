import allure
import pytest

from src.helpers.api_requests_wrappers import post_request
from src.constants.api_constants import APIconstants
from src.helpers.payload_manager import payload_create_booking, payload_create_token
from src.helpers.common_verification import *
from src.utils.utils import Utils

@pytest.fixture(scope="session")
def create_token():
    response = post_request(
        url=APIconstants().url_create_token(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_token(),
        in_json=False
    )

    # verification
    verify_status_code(response_data=response, expected_data=200)
    verify_for_token_not_null(response.json()["token"])
    return response.json()["token"]

@pytest.fixture(scope="session")
def get_booking_id():
    response = post_request(
        url=APIconstants().url_create_booking(),
        auth=None,
        headers=Utils().common_headers_json(),
        payload=payload_create_booking(),
        in_json=False
    )
    booking_id = response.json()["bookingid"]

    # verification
    verify_status_code(response_data=response, expected_data=200)
    verify_json_key_not_null(response.json()["booking_id"])
    return booking_id

