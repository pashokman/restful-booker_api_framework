import pytest

from data.endpoints import PARTIAL_UPDATE_BOOKING_ENDPOINT
from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, partial_update_boking, api_client

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    yield token, booking_id

    delete_booking(booking_id, token)


@pytest.mark.partial_update_booking
@pytest.mark.security
class TestPartialUpdateBookingSecurity():

    @pytest.fixture(autouse=True)
    def setup(self, prepare):
        self.token, self.booking_id = prepare


    def test_partial_update_booking_token_plus_1_end_symbol(self):
        token = self.token + 'w'
        part_upd_resp = partial_update_boking(self.booking_id, {'firstname': 'Joey'}, token)
        assert_status_code(part_upd_resp.status_code, 403)


    def test_partial_update_booking_token_without_last_symbol(self):
        token = self.token[:-1]
        part_upd_resp = partial_update_boking(self.booking_id, {'firstname': 'Joey'}, token)
        assert_status_code(part_upd_resp.status_code, 403)


    def test_partial_update_booking_token_without_first_symbol(self):
        token = self.token[1:]  
        part_upd_resp = partial_update_boking(self.booking_id, {'firstname': 'Joey'}, token)
        assert_status_code(part_upd_resp.status_code, 403)


    def test_partial_update_booking_with_empty_token(self):
        token = ''
        part_upd_resp = partial_update_boking(self.booking_id, {'firstname': 'Joey'}, token)
        assert_status_code(part_upd_resp.status_code, 403)


    def test_partial_update_booking_without_headers(self):       
        part_upd_resp = api_client.patch(PARTIAL_UPDATE_BOOKING_ENDPOINT(self.booking_id), {'firstname': 'Joey'})
        assert_status_code(part_upd_resp.status_code, 403)
