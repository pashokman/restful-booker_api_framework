#           Auth
# -----CreateToken
AUTH_ENDPOINT = '/auth'

#           Booking
# -----GetBookingIds
GET_BOOKING_IDS_ENDPOINT = '/booking'

# -----GetBooking
def GET_BOOKING_ENDPOINT(bookingid):
    return f'/booking/{bookingid}'

# -----CreateBooking
CREATE_BOOKING_ENDPOINT = '/booking'

# -----UpdateBooking
def UPDATE_BOOKING_ENDPOINT(bookingid):
    return f'/booking/{bookingid}'

# -----PartialUpdateBooking
def PARTIAL_UPDATE_BOOKING_ENDPOINT(bookingid):
    return f'/booking/{bookingid}'

# -----DeleteBooking
def DELETE_BOOKING_ENDPOINT(bookingid):
    return f'/booking/{bookingid}'

#           Ping
# -----HealthCheck
HEALTH_CHECK_ENDPOINT = '/ping'