# Скрипт для отримання списку безкоштовних проксі
# Мета: Витягнути актуальний список HTTP, HTTPS, SOCKS4, SOCKS5 проксі з відкритих джерел

import requests
import json

# URL для отримання списку проксі (наприклад, Proxifly)
proxy_list_url = "https://cdn.jsdelivr.net/gh/proxifly/free-proxy-list@main/proxies/all/data.txt"

# Функція для отримання списку проксі
def fetch_proxy_list():
    try:
        response = requests.get(proxy_list_url, timeout=10)
        if response.status_code == 200:
            proxies = response.text.splitlines()
            return proxies
        else:
            print(f"Помилка при отриманні списку: {response.status_code}")
            return []
    except Exception as e:
        print(f"Помилка: {e}")
        return []

# Функція для збереження списку у файл
def save_proxy_list(proxies):
    with open("free_proxy_list.txt", "w") as file:
        for proxy in proxies:
            file.write(f"{proxy}\n")
    print("Список проксі збережено у free_proxy_list.txt")

# Функція для фільтрації проксі за типом (HTTP, HTTPS, SOCKS4, SOCKS5)
def filter_proxies(proxies, protocol=None):
    filtered = []
    for proxy in proxies:
        if protocol:
            if protocol.lower() in proxy.lower():
                filtered.append(proxy)
        else:
            filtered.append(proxy)
    return filtered

# Основна функція
def main():
    print("Отримання списку безкоштовних проксі...")
    proxies = fetch_proxy_list()
    if proxies:
        # Фільтрація за HTTPS-проксі (можна змінити на SOCKS4, SOCKS5 або залишити без фільтра)
        filtered_proxies = filter_proxies(proxies, protocol="https")
        save_proxy_list(filtered_proxies)
        print(f"Отримано {len(filtered_proxies)} проксі. Приклад перших 5:")
        for proxy in filtered_proxies[:5]:
            print(proxy)
    else:
        print("Не вдалося отримати список проксі.")

if __name__ == "__main__":
    main()

# Пояснення:
# Цей скрипт витягує список безкоштовних проксі з відкритого джерела (Proxifly, яке оновлюється кожні 5-20 хвилин).
# Він зберігає проксі у файл free_proxy_list.txt і дозволяє фільтрувати за типом (наприклад, HTTPS). Ви можете
# запустити цей скрипт на будь-якому комп’ютері з Python та бібліотекою requests. Список включає IP-адреси та порти,
# наприклад: 123.45.67.89:8080. Для використання проксі перевірте їхню працездатність через інструменти, такі як
# Elite Proxy Switcher, оскільки безкоштовні проксі часто ненадійні.