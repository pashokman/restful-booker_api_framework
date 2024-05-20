# restful-booker_api_framework

## Steps of creating an API framework
1. Create project folder structure:
```
restful-booker_api_framework/
── data/
── tests/
    ── __init__.py
    ── test_auth.py
    ── test_booking.py
    ── test_health_check.py
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
```
6. Create virtual environment - ```python -m venv venv```
7. Change environment to a virtual newly created environment - ```venv\Scripts\activate```
8. In ```requirements.txt``` should save additional packages names. To install all needed packages from file, use command:
```
pip install -r requirements.txt
```
9. Create test files in tests folder, separated by controlers.