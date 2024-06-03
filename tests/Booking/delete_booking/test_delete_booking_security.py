import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import *

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture(scope='class')
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    yield token, booking_id

    delete_booking(booking_id, token)


@pytest.mark.delete_booking
@pytest.mark.security
class TestDeleteBookingSecurity():

    @pytest.fixture(autouse=True)
    def setup(self, prepare):
        self.token, self.booking_id = prepare


    def test_delete_booking_token_plus_1_end_symbol(self):
        token = self.token + 'w'
        del_resp = delete_booking(self.booking_id, token)
        assert_status_code(del_resp.status_code, 403)


    def test_delete_booking_token_without_last_symbol(self):
        token = self.token[:-1]
        del_resp = delete_booking(self.booking_id, token)
        assert_status_code(del_resp.status_code, 403)


    def test_delete_booking_token_without_first_symbol(self):
        token = self.token[1:]
        del_resp = delete_booking(self.booking_id, token)
        assert_status_code(del_resp.status_code, 403)


    def test_delete_booking_with_empty_token(self):
        token = ''
        del_resp = delete_booking(self.booking_id, token)
        assert_status_code(del_resp.status_code, 403)


    def test_delete_booking_without_headers(self):
        del_booking = api_client.delete(DELETE_BOOKING_ENDPOINT(self.booking_id))
        assert_status_code(del_booking.status_code, 403)
