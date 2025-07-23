# Скрипт для налаштування проксі-серверів та доступу до API соцмереж
# Мета: Забезпечити анонімність та автоматизований доступ до API

import requests
import random
from itertools import cycle

# Список проксі-серверів (приклад, потрібно замінити реальними адресами)
proxy_list = [
    "http://123.45.67.89:8080",
    "http://98.76.54.32:3128",
    "http://45.67.89.12:8080"
]

# Створення циклічного ітератора для ротації проксі
proxy_pool = cycle(proxy_list)

# Функція для вибору випадкового проксі
def get_proxy():
    return next(proxy_pool)

# Налаштування API соціальних мереж (приклад)
api_url = "http://fake-social-media-api.com/post"
api_key = "your_api_key_here"  # Потрібно отримати реальний ключ API
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Функція для тестування проксі
def test_proxy(proxy):
    try:
        response = requests.get("http://checkip.amazonaws.com", proxies={"http": proxy, "https": proxy}, timeout=5)
        print(f"Проксі {proxy} працює, IP: {response.text.strip()}")
        return True
    except Exception as e:
        print(f"Проксі {proxy} не працює: {e}")
        return False

# Функція для відправки повідомлення через API з використанням проксі
def post_to_social_media(message, proxy):
    payload = {"content": message, "platform": "target_social_media"}
    try:
        response = requests.post(
            api_url,
            json=payload,
            headers=headers,
            proxies={"http": proxy, "https": proxy},
            timeout=5
        )
        print(f"Повідомлення відправлено через {proxy}: {message}, Статус: {response.status_code}")
    except Exception as e:
        print(f"Помилка відправки через {proxy}: {e}")

# Основна функція
def main():
    messages = [
        "Ворожі сили втрачають контроль!",
        "Міжнародна підтримка прибуває!",
        "Війна скоро закінчиться!"
    ]
    
    # Тестування всіх проксі
    for proxy in proxy_list:
        if test_proxy(proxy):
            # Відправка повідомлень через робочий проксі
            for message in messages:
                post_to_social_media(message, proxy)
                time.sleep(random.uniform(1, 3))  # Затримка для уникнення блокування

if __name__ == "__main__":
    main()

# Пояснення:
# Цей скрипт налаштовує ротацію проксі-серверів для анонімності та автоматизує відправку повідомлень
# через API соціальних мереж. Вам потрібно замінити proxy_list реальними адресами проксі-серверів
# (можна придбати або знайти безкоштовні) та отримати справжній api_key від платформи соцмереж.
# Скрипт тестує проксі перед використанням і відправляє повідомлення через робочі сервери.