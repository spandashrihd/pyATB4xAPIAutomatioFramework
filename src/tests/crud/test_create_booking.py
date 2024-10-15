import logging
from http.client import responses
from logging import logThreads

import allure
import pytest

from src.helpers.api_requests_wrappers import post_request
from src.constants.api_constants import APIconstants
from src.helpers.payload_manager import payload_create_booking
from src.helpers.common_verification import *
from src.utils.utils import Utils

class TestCreateBooking():
    @pytest.mark.positive
    @allure.title("Verify that create booking status and booking Id should not be null")
    @allure.description("Create a booking from payload and verify that booking id should ot be null")
    def test_create_booking_positive(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting of the TC1 - Positive")
        response = post_request(
            url=APIconstants().url_create_booking(),
            auth=None,
            header=Utils().common_headers_json(),
            payload=payload_create_booking(),
            in_json=False
        )

        # verification
        verify_status_code(response_data=response, expected_data=200)
        verify_json_key_not_null(response.json()["booking_id"])
        LOGGER.info(response.json()["booking_id"])
        LOGGER.info("End of the TC1 - Positive")

    @pytest.mark.negative
    @allure.title("Verify that create booking does not work with no payload")
    @allure.description("Create a booking with no payload")
    def test_create_booking_negative(self):
        LOGGER=logging.getLogger(__name__)
        LOGGER.info("Starting of the TC2 - Negative")
        response = post_request(
            url=APIconstants().url_create_booking(),
            auth=None,
            header=Utils().common_headers_json(),
            payload={},
            in_json=False
        )

        # verification
        verify_status_code(response_data=response, expected_data=200)
        LOGGER.info("End of the TC1 - Positive")



