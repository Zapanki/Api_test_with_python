import requests
import pytest


@pytest.mark.apitest
def test_get_locations_for_us_90210_check_status_code_equals_200():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    assert response.status_code == 200


def test_get_locations_for_us_90210_check_content_type_equals_json():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    assert response.headers['Content-Type'] == "application/json"


def test_get_locations_for_us_90210_check_country_equals_united_states():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    response_body = response.json()
    assert response_body["country"] == "Russia"


def test_get_locations_for_us_90210_check_city_equals_beverly_hills():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    response_body = response.json()
    assert response_body["places"][0]["place name"] == "Москва"


def test_get_locations_for_us_90210_check_one_place_is_returned():
    response = requests.get("http://api.zippopotam.us/RU/101000")
    response_body = response.json()
    assert len(response_body["places"]) == 1