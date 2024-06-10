import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, update_booking

from utils.assertions.assert_status_code import assert_status_code


@pytest.fixture
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json['bookingid']

    changed_data = copy.deepcopy(UPDATE_BOOKING_DATA)

    yield token, booking_id, changed_data

    delete_booking(booking_id, token)


@pytest.mark.update_booking
class TestUpdateBookingWithoutMandatoryFields():

    @pytest.fixture(autouse=True)
    def setup(self, prepare):
        self.token, self.booking_id, self.changed_data = prepare


    def test_update_booking_without_firstname(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.pop('firstname', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_lastname(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.pop('lastname', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_totalprice(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.pop('totalprice', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_depositpaid(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.pop('depositpaid', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_bookingdates(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.pop('bookingdates', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_bookingdates_checkin(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.get('bookingdates', 'Key not exist').pop('checkin', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)


    def test_update_booking_without_bookingdates_checkout(self):
        new_changed_data = copy.deepcopy(self.changed_data)
        new_changed_data.get('bookingdates', 'Key not exist').pop('checkout', 'Key not exist')

        update_resp = update_booking(self.booking_id, new_changed_data, self.token)
        assert_status_code(update_resp.status_code, 400)
