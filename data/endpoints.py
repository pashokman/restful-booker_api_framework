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

# -----PartialUpdateBooking

# -----DeleteBooking


#           Ping
# -----HealthCheck