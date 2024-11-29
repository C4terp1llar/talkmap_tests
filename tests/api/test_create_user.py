def test_create_user(api_client):
    user_data = {
        "email": "test_api@yandex.ru",
        "password": "TestPassword123",
        "nickname": "testing_api",
        "date_b": "2000-12-12",
        "gender": "Мужской",
        "avatar": "https://i.ibb.co/DVxdj17/v11.png",
        "address": {
            "display_name": "Crona, 427, улица Ленина, Промышленный район, Ставрополь, городской округ Ставрополь, Ставропольский край, Северо-Кавказский федеральный округ, 355000, Россия",
            "lat": 45.03897775,
            "lon": 41.91683894797461,
            "type": "apartments",
            "address_type": "building",
            "name": "Crona",
            "city": "Ставрополь",
            "house_number": 427,
            "road": "улица Ленина",
            "city_district": "Промышленный район",
            "state": "Ставропольский край",
            "country": "Россия",
            "country_code": "ru",
            "boundingbox": [
                "45.0384258",
                "45.0394017",
                "41.9154680",
                "41.9169863"
            ]
        },
        "device_info": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36&ru-RU&1732861775244"
    }

    response = api_client.post("/reg/registerUser", data=user_data)

    assert response.status_code == 201, f"Ожидался статус 201, но получили {response.status_code}"

    response_json = response.json()

    assert response_json["message"] == "Пользователь зарегистрирован", "Некорректное сообщение по итогам регистрации"
    assert response_json.get("accessToken") is not None, "Отсутствует access токен после регистрации"


