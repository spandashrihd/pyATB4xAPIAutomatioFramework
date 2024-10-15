#create token
#create booking id
#update teh booking(put) - booking id, token
#delete teh booking
from cgitb import reset
from http.client import responses

#verify that created booking id, when we update we are able to update it and delete it also

import allure
import pytest

from src.helpers.api_requests_wrappers import post_request
from src.constants.api_constants import APIconstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils


class TestCRUDBooking():
    @allure.title("Test CRUD operation update(PUT)")
    @allure.description("Verify that full update with booking ID and token is working")
    def test_update_booking_id_token(self,create_token,get_booking_id):

        put_url=APIconstants().url_put_patch_delete(booking_id=get_booking_id)
        response=post_request(
            url=put_url,
            headers=Utils().common_headers_put_patch_delete_cookie(token=create_token),
            payload=payload_create_booking(),
            auth=None,
            in_json=False
        )

        # verification
        verify_status_code(response_data=response, expected_data=200)
        verify_response_key(response.json()["firstname"], "Jim")
        verify_response_key(response.json()["lastname"], "Brown")



    def test_delete_booking_id(self):
        pass



