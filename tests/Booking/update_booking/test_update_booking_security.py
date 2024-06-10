import pytest

from data.endpoints import UPDATE_BOOKING_ENDPOINT
from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, update_booking, api_client

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    yield token, booking_id

    delete_booking(booking_id, token)


@pytest.mark.update_booking
@pytest.mark.security
class TestUpdateBookingSecurity():

    @pytest.fixture(autouse=True)
    def setup(self, prepare):
        self.token, self.booking_id = prepare


    def test_update_booking_token_plus_1_end_symbol(self):
        token = self.token + 'w'
        update_resp = update_booking(self.booking_id, UPDATE_BOOKING_DATA, token)
        assert_status_code(update_resp.status_code, 403)


    def test_update_booking_token_without_last_symbol(self):
        token = self.token[0:-1]
        update_resp = update_booking(self.booking_id, UPDATE_BOOKING_DATA, token)
        assert_status_code(update_resp.status_code, 403)


    def test_update_booking_token_without_first_symbol(self):
        token = self.token[1:]
        
        update_resp = update_booking(self.booking_id, UPDATE_BOOKING_DATA, token)
        assert_status_code(update_resp.status_code, 403)


    def test_update_booking_with_empty_token(self):
        token = ''
        update_resp = update_booking(self.booking_id, UPDATE_BOOKING_DATA, token)
        assert_status_code(update_resp.status_code, 403)


    def test_update_booking_without_headers(self):        
        update_resp = api_client.put(UPDATE_BOOKING_ENDPOINT(self.booking_id), UPDATE_BOOKING_DATA)
        assert_status_code(update_resp.status_code, 403)
