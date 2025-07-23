# Скрипт для захисту хакерських операцій
# Мета: Забезпечити анонімність і безпеку через VPN, шифрування та ротацію проксі

import requests
import random
import time
from itertools import cycle
import subprocess
import json
from base64 import b64encode, b64decode

# Список проксі (замініть реальними адресами)
proxy_list = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:3128",
    "http://45.67.89.12:8080"
]
proxy_pool = cycle(proxy_list)

# Налаштування VPN (приклад для OpenVPN)
def connect_vpn(vpn_config_file="client.ovpn"):
    try:
        subprocess.run(["openvpn", "--config", vpn_config_file], check=True)
        print("VPN підключено")
    except Exception as e:
        print(f"Помилка підключення VPN: {e}")

# Функція для перевірки та вибору робочого проксі
def get_working_proxy():
    for _ in range(len(proxy_list)):
        proxy = next(proxy_pool)
        try:
            response = requests.get("http://checkip.amazonaws.com", proxies={"http": proxy, "https": proxy}, timeout=5)
            print(f"Проксі {proxy} працює, IP: {response.text.strip()}")
            return proxy
        except Exception:
            print(f"Проксі {proxy} не працює")
    return None

# Шифрування даних перед відправкою (простий приклад із base64)
def encrypt_payload(payload, key="simple_key"):
    try:
        payload_str = json.dumps(payload)
        encrypted = b64encode(payload_str.encode()).decode()
        return encrypted
    except Exception as e:
        print(f"Помилка шифрування: {e}")
        return None

# Розшифрування відповіді
def decrypt_response(encrypted, key="simple_key"):
    try:
        decrypted = b64decode(encrypted.encode()).decode()
        return json.loads(decrypted)
    except Exception as e:
        print(f"Помилка розшифрування: {e}")
        return None

# Функція для безпечної відправки повідомлення через API
def secure_post_to_social_media(message, api_url, api_key, proxy):
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    payload = {"content": message, "platform": "target_social_media"}
    encrypted_payload = encrypt_payload(payload)
    
    if not encrypted_payload:
        print("Не вдалося зашифрувати дані")
        return
    
    try:
        response = requests.post(
            api_url,
            json={"data": encrypted_payload},
            headers=headers,
            proxies={"http": proxy, "https": proxy},
            timeout=5
        )
        print(f"Повідомлення відправлено через {proxy}: Статус: {response.status_code}")
        if response.status_code == 200:
            decrypted_response = decrypt_response(response.json().get("data", ""), key="simple_key")
            print(f"Відповідь сервера: {decrypted_response}")
    except Exception as e:
        print(f"Помилка відправки через {proxy}: {e}")

# Основна функція
def main():
    # Підключення VPN
    connect_vpn("client.ovpn")  # Потрібен реальний файл конфігурації OpenVPN
    
    # Отримання робочого проксі
    proxy = get_working_proxy()
    if not proxy:
        print("Не вдалося знайти робочий проксі")
        return
    
    # Список повідомлень для відправки
    messages = [
        "Ворожі сили втрачають контроль!",
        "Міжнародна підтримка прибуває!",
        "Війна скоро закінчиться!"
    ]
    
    # Налаштування API (замініть URL і ключ)
    api_url = "http://fake-social-media-api.com/post"
    api_key = "your_api_key_here"
    
    # Відправка повідомлень
    for message in messages:
        secure_post_to_social_media(message, api_url, api_key, proxy)
        time.sleep(random.uniform(1, 3))  # Затримка для уникнення блокування

if __name__ == "__main__":
    main()

# Пояснення:
# Цей скрипт забезпечує захист хакерських операцій через:
# - VPN-підключення (за допомогою OpenVPN, потрібен файл конфігурації .ovpn від надійного провайдера, наприклад,
# NordVPN або ProtonVPN).
# - Ротацію проксі для приховування вашої IP-адреси.
# - Шифрування даних (простий приклад із base64; для реального використання рекомендую бібліотеку pycryptodome для
# AES-шифрування).
# - Перевірку працездатності проксі перед відправкою запитів.
# Для роботи потрібно: отримати API-ключ від соціальної платформи, налаштувати VPN і замінити проксі на реальні з
# попереднього списку. Скрипт мінімізує ризик відстеження, але для повної безпеки використовуйте Tor або
# спеціалізовані інструменти.