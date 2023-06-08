import requests
import data
import configuration

# Анна Первухина, 5-я когорта — Финальный проект. Инженер по тестированию плюс

def create_new_order():
    url = configuration.URL_SERVICE + configuration.CREATE_ORDER
    order_response = requests.post(url,
                             json=data.order_body)
    return order_response

def test_get_order_by_track():
    response = create_new_order()
    assert response.status_code == 201

    track_number = response.json()['track']
    track_url = configuration.URL_SERVICE + configuration.GETTING_ORDER_BY_TRACK + "?t=" + str(track_number)
    response = requests.get(track_url)
    assert response.status_code == 200

    if response.status_code == 200:
        print("Тест пройден")
    else:
        print("Тест провален")

