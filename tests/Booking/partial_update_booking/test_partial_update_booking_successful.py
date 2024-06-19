import copy
import pytest

from data.auth.auth_objects import AUTH_DATA
from data.booking.booking_objects import NEW_BOOKING_DATA, UPDATE_BOOKING_DATA

from utils.methods.authorization import authorization
from utils.methods.booking import create_booking_json, delete_booking, partial_update_boking, get_booking_json

from utils.assertions.assert_status_code import assert_status_code
from utils.assertions.assert_json_object import assert_json_object


pytestmark = [pytest.mark.partial_update_booking, pytest.mark.success]


@pytest.fixture
def prepare():
    token = authorization(AUTH_DATA)

    create_resp_json = create_booking_json(NEW_BOOKING_DATA)
    booking_id = create_resp_json.get('bookingid', 'Key not exist')

    yield token, booking_id

    delete_booking(booking_id, token)


def test_partial_update_booking_all_params_successful(prepare):
    token, booking_id = prepare

    part_upd_resp = partial_update_boking(booking_id, UPDATE_BOOKING_DATA, token)
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), UPDATE_BOOKING_DATA)
    assert_json_object(get_resp_json, UPDATE_BOOKING_DATA)


def test_partial_update_booking_firstname_param_successful(prepare):
    token, booking_id = prepare

    firstname = 'Trevor'
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['firstname'] = firstname
    
    update_data = {'firstname': firstname}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)

    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_lastname_param_successful(prepare):
    token, booking_id = prepare

    lastname = 'Kollins'
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['lastname'] = lastname

    update_data = {'lastname': lastname}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_totalprice_param_successful(prepare):
    token, booking_id = prepare

    totalprice = 2345
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['totalprice'] = totalprice

    update_data = {'totalprice': totalprice}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_depositpaid_param_successful(prepare):
    token, booking_id = prepare

    depositpaid = False
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['depositpaid'] = depositpaid

    update_data = {'depositpaid': depositpaid}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_bookingdates_param_successful(prepare):
    token, booking_id = prepare

    bookingdates = {
        "checkin" : "2023-11-15",
        "checkout" : "2023-11-16"
    }
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates'] = bookingdates

    update_data = {'bookingdates': bookingdates}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_bookingdates_checkin_param_successful(prepare):
    token, booking_id = prepare

    checkin = "2023-11-15"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates']['checkin'] = checkin
    exp_booking['bookingdates']['checkout'] = '0NaN-aN-aN'

    update_data = {'bookingdates':{'checkin': checkin}}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_bookingdates_checkout_param_successful(prepare):
    token, booking_id = prepare

    checkout = "2023-11-15"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['bookingdates']['checkin'] = '0NaN-aN-aN'
    exp_booking['bookingdates']['checkout'] = checkout

    update_data = {'bookingdates':{'checkout': checkout}}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)


def test_partial_update_booking_additionalneeds_param_successful(prepare):
    token, booking_id = prepare

    additionalneeds = "2 sofas"
    exp_booking = copy.deepcopy(NEW_BOOKING_DATA)
    exp_booking['additionalneeds'] = additionalneeds

    update_data = {'additionalneeds': additionalneeds}
    part_upd_resp = partial_update_boking(booking_id, update_data, token)
    
    get_resp_json = get_booking_json(booking_id)

    assert_status_code(part_upd_resp.status_code, 200)
    assert_json_object(part_upd_resp.json(), exp_booking)
    assert_json_object(get_resp_json, exp_booking)
