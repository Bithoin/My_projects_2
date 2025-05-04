import aiohttp
import asyncio
import logging
from typing import List, Dict, Optional

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('user_search.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)
BASE_URL = "https://jsonplaceholder.typicode.com"


async def fetch_users_by_name(session: aiohttp.ClientSession, name: str) -> Optional[List[Dict]]:
    url = f"{BASE_URL}/users?username={name}"
    try:
        logger.info(f"Відправляємо запит для пошуку: {name}")
        async with session.get(url) as response:
            if response.status == 200:
                users = await response.json()
                logger.info(f"Отримано {len(users)} результатів для {name}")
                return users
            else:
                logger.error(f"Помилка запиту для {name}: статус {response.status}")
                return None
    except aiohttp.ClientError as e:
        logger.error(f"Помилка підключення для {name}: {str(e)}")
        return None
    except Exception as e:
        logger.error(f"Неочікувана помилка для {name}: {str(e)}")
        return None


async def search_users(names: List[str]) -> Dict[str, Optional[List[Dict]]]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_users_by_name(session, name) for name in names]
        results = await asyncio.gather(*tasks)
        return dict(zip(names, results))


def display_user_info(users: List[Dict]) -> None:
    for user in users:
        print("\n" + "=" * 50)
        print(f"ID: {user['id']}")
        print(f"Ім'я: {user['name']}")
        print(f"Ім'я користувача: {user['username']}")
        print(f"Email: {user['email']}")
        print(f"Адреса:")
        print(f"  Вулиця: {user['address']['street']}")
        print(f"  Квартира: {user['address']['suite']}")
        print(f"  Місто: {user['address']['city']}")
        print(f"  Поштовий код: {user['address']['zipcode']}")
        print(f"  Геолокація: ({user['address']['geo']['lat']}, {user['address']['geo']['lng']})")
        print(f"Телефон: {user['phone']}")
        print(f"Вебсайт: {user['website']}")
        print(f"Компанія: {user['company']['name']}")
        print(f"  Кредо: {user['company']['catchPhrase']}")
        print(f"  Бізнес: {user['company']['bs']}")
        print("=" * 50 + "\n")


async def main():
    print("Асинхронний пошук користувачів на JSONPlaceholder")
    search_names = ["Bret", "Antonette", "Samantha", "Karianne", "Kamren", "Leopoldo_Corkery"]
    logger.info(f"Початок пошуку для: {', '.join(search_names)}")
    results = await search_users(search_names)
    total_found = 0
    for name, users in results.items():
        if users:
            print(f"\nЗнайдено {len(users)} користувачів з іменем '{name}':")
            display_user_info(users)
            total_found += len(users)
        else:
            print(f"\nКористувачів з іменем '{name}' не знайдено.")
    logger.info(f"Пошук завершено. Знайдено {total_found} користувачів всього.")
if __name__ == "__main__":
    asyncio.run(main())