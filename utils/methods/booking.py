from data.endpoints import CREATE_BOOKING_ENDPOINT, GET_BOOKING_ENDPOINT, DELETE_BOOKING_ENDPOINT


def create_booking(api_client, booking_data):
    booking = api_client.post(CREATE_BOOKING_ENDPOINT, booking_data)
    return booking


def create_booking_json(api_client, booking_data):
    booking = api_client.post(CREATE_BOOKING_ENDPOINT, booking_data)
    return booking.json()


def delete_booking(api_client, booking_id, token):
    headers = {'Cookie': f'token={token}'}
    delete = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    return delete


def delete_booking_json(api_client, booking_id, token):
    headers = {'Cookie': f'token={token}'}
    delete = api_client.delete(DELETE_BOOKING_ENDPOINT(booking_id), headers=headers)
    return delete.json()


def get_booking(api_client, booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp


def get_booking_json(api_client, booking_id):   
    get_resp = api_client.get(GET_BOOKING_ENDPOINT(booking_id))
    return get_resp.json()