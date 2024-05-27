# restful-booker_api_framework

## Steps of creating an API framework
1. Create project folder structure:
```
restful-booker_api_framework/
── data/
── tests/
    ── __init__.py
    ── auth/
        ── __init__.py
        ── create_token/
            ── __init__.py
            ── test_auth.py
    ── booking/
        ── __init__.py
        ── create_booking/
        ── delete_booking/
        ── get_booking/
...
── utils/
    ── __init__.py
    ── api_client.py
    ── config.py
── conftest.py
── pytest.ini
── requirements.txt
── readme.md
```
2. In ```utils/config.py``` save BASE_API_URL as BASE_URL.
3. In ```utils/api_client.py``` create a class APIClient with main API methods impementation.
4. In ```conftest.py``` create a fixture, which returns APIClient instance with 'session' scope.
5. In ```pytest.ini``` save additional options of testrun:
```
[pytest]
addopts = --maxfail=2
markers =
    success: Test successful method running
    auth: Test authorization method
```
6. Create virtual environment - ```python -m venv venv```
7. Change environment to a virtual newly created environment - ```venv\Scripts\activate```
8. In ```requirements.txt``` should save additional packages names. To install all needed packages from file, use command:
```
pip install -r requirements.txt
```
9. Create test files in method name folder in tests folder, all methods shoulld be separated by controllers, like in documentation.


## Implemented test list
All API consists of controllers - Auth, Booking, Ping. Every controler consists of it's methods.

### Auth
* generate token with correct credentials
* generate token without credentials
* generate token invalid username and valid password
* generate token invalid password and valid username

### Booking
* Get booking IDs
    + get booking ids successfuly:
        - get booking ids by firstname and lastname
        - get booking ids by firstname
        - get booking ids by lastname
        - get booking ids by checkin
        - get booking ids by checkout
    + get booking ids by non existing params:
        - by non existing firstname
        - by non existing lastname
        - by non existing checkin
        - by non existing checkout

* Get booking
    + get booking successfuly
    + get non existing booking:
        - get booking with id = 999999
        - get booking with id = 0

* Create booking
    + create booking successfuly
    + create booking without mandatory fields:
        - without firstname
        - without lastname
        - without totalprice
        - without depositpaid
        - without bookingdates
        - without bookingdates
        - without bookingdates-checkin
        - without bookingdates-checkout
    + create booking without additional field - additionalneeds
    + create booking with incorrect parameters data types:
        - firstname not string
        - lastname not string
        - totalprice not number
        - totalprice not integer
        - depositpaid not boolean
        - bookingdates not dictionary
        - bookingdates-checkin not date
        - bookingdates-checkout not date
        - additionalneeds not string
    + create booking with logical errors:
        - totalprice = 0
        - totalprice < 0
        - bookingdates-checkout < bookingdates-checkin

* Update booking
    + update booking security:
        - update booking token and 1 symbol
        - update booking token without last symbol
        - update booking token without first symbol
        - update booking without token
        - update booking without headers
    + update booking successfuly
    + update booking without mandatory fields:
        - update booking without firstname
        - update booking without lastname
        - update booking without totalprice
        - update booking without depositpaid
        - update booking without bookingdates
        - update booking without bookingdates-checkin
        - update booking without bookingdates-checkout
    + update booking without additional field - additionalneeds

* Partical update booking
    + partial update booking security:
        - partial update booking token and 1 symbol
        - partial update booking token without last symbol
        - partial update booking token without first symbol
        - partial update booking without token
        - partial update booking without headers
    + partial update booking success:
        - partial update booking with all params
        - partial update booking firstname param
        - partial update booking lastname param
        - partial update booking totalprice param
        - partial update booking depositpaid param
        - partial update booking bookingdates param
        - partial update booking bookingdates-checkin param
        - partial update booking bookingdates-checkout param
        - partial update booking additionalneeds param

* Delete booking
    + delete booking security:
        - delete booking token and 1 symbol
        - delete booking token without last symbol
        - delete booking token without first symbol
        - delete booking without token
        - delete booking without headers
    + delete booking successfuly
    + delete unexisting booking

### Ping
* Health check
    + health check successful

The list of test should be larger, but this API is not completed enough to make all tests.

## Most used commands for testing and debugging
Example of a request:
```
import requests

data = {
    "firstname": "Lester",
    "lastname": "Tester"
}

response = requests.post('https://restful-booker.herokuapp.com/booking/', json=data, headers=headers)
```
1. ```response.status_code``` - returns a status code of a request response
2. ```response.json()``` - returns a response body like a JSON object 
3. ```response.text``` - returns a response body like a string
4. ```response.url``` - returns the urls of the request
5. ```response.request.body``` - returns a body of the request in a byte format
6. ```response.request.body.decode("utf-8")``` - returns a body of the request in a string format
7. ```response.request.headers``` - returns headers of the request
8. Should use ```deepcopy``` command for creating a new copy of the data to change it whithout changing the original data:
```
import copy

data = {
    "firstname": "Lester",
    "lastname": "Tester"
}

# creates a new data object
new_data = copy.deepcopy(data) 
```

# Commands to run tests
* ```pytest``` - run all tests
* ```pytest -m <mark_name>``` - run all tests with specific mark
* ```pytest -m '<mark_name1> and <mark_name2>'``` - run all tests with specific both marks 1 and 2
* ```pytest -m '<mark_name1> or <mark_name2>'``` - run all tests with one of specific marks 1 and 2