import sys
import os
import re
import shodan
import asyncio
import json
import time
from mcstatus import JavaServer
from rich.console import Console
from ipaddress import IPv4Address
from typing import List, Tuple
from colorama import Fore, Style, init

# Инициализация coloramaи
init(autoreset=True)

# Логотип программы
LOGO = f"""
{Fore.LIGHTRED_EX}
 _____           ___  ________  _____ _               _             
|  __ \          |  \/  /  __ \/  ___| |             | |            
| |  \/ ___ _ __ | .  . | /  \/\ `--.| |__   ___   __| | __ _ _ __  
| | __ / _ \ '_ \| |\/| | |     `--. \ '_ \ / _ \ / _` |/ _` | '_ \ 
| |_\ \  __/ | | | |  | | \__/\/\__/ / | | | (_) | (_| | (_| | | | |
 \____/\___|_| |_\_|  |_/\____/\____/|_| |_|\___/ \__,_|\__,_|_| |_| 

                                                                                                                                  
"""

# Инициализация консоли
console = Console()

# Функция для отображения сообщения об ошибке
def display_error():
    print(center_text(LOGO))
    print()
    print(center_text(f"""
    {Fore.LIGHTYELLOW_EX}╭────────────────────────────━━━━━━━━━━━━━━━━━━━━━━────────────────────────╮
| {Fore.LIGHTGREEN_EX}Use » python {os.path.basename(__file__)} [Порт] [Путь к файлу результата] [Поисковый запрос] {Fore.LIGHTYELLOW_EX}| 
╰────────────────────────────━━━━━━━━━━━━━━━━━━━━━━────────────────────────╯
    """))
    sys.exit()

def center_text(text):
    lines = text.strip().split("\n")
    max_length = max(len(line) for line in lines)
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - max_length) // 2
    centered_lines = [(" " * padding) + line for line in lines]
    return "\n".join(centered_lines)

# Чтение API ключа из конфигурационного файла
def load_api_key(config_path="config.json"):
    with open(config_path, 'r') as file:
        config = json.load(file)
        return config.get("SHODAN_API_KEY")

# Очистка консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

# Разбор аргументов командной строки
try:
    PORT = int(sys.argv[1])
    RESULT_FILE = sys.argv[2]
    SEARCH_QUERY = sys.argv[3]
    clear_console()
    print(center_text(LOGO))
    print(f"\n{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Начинаю поиск...")
except IndexError:
    display_error()

SHODAN_API_KEY = load_api_key()
found_ips = 0

# Функция для получения информации о Minecraft сервере
async def gather_mc_info(ip: IPv4Address, port: int) -> None:
    global found_ips
    try:
        server = await JavaServer(host=ip.compressed, port=port).async_status()
        motd_clean = re.sub(r'§[0-9a-fk-or]', '', ''.join(
            x.split("'")[0] for x in str(server.description).split("'text':'")
        ))
        with open(RESULT_FILE, "a", encoding="utf-8") as file:
            result_line = f'[+] {ip}:{port} ({server.version.name})({server.players.online}/{server.players.max})({motd_clean})\n'
            print(result_line)
            file.write(result_line)
        found_ips += 1
    except (UnicodeEncodeError, ConnectionRefusedError):
        pass
    except Exception as e:
        print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Ошибка при получении данных для {Fore.LIGHTGREEN_EX}{ip}:{port} {Fore.LIGHTBLUE_EX}- {Fore.LIGHTRED_EX}{e}")

# Функция для поиска по Shodan с использованием указанного запроса
async def shodan_search(query: str, client: shodan.Shodan) -> List[Tuple[IPv4Address, int]]:
    results = client.search(query=query)
    return [(IPv4Address(result['ip_str']), int(result['port'])) for result in results['matches']]

# Основная функция для координации операций поиска и получения информации о серверах
async def main():
    start_time = time.time()
    try:
        shodan_client = shodan.Shodan(SHODAN_API_KEY)
    except shodan.APIError as e:
        print(f'{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Неверный или просроченный Shodan API ключ: {Fore.LIGHTRED_EX}{e}')
        return

    results = await shodan_search(SEARCH_QUERY, shodan_client)
    await asyncio.gather(*(gather_mc_info(ip, port) for ip, port in results))

    # Завершающее сообщение с информацией о сканировании
    elapsed_time = time.time() - start_time
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Сканирование заняло {Fore.LIGHTGREEN_EX}{elapsed_time:.2f} {Fore.LIGHTBLUE_EX}секунд")
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Найдено IP: {Fore.LIGHTGREEN_EX}{found_ips}")
    print(f"{Fore.LIGHTYELLOW_EX}[ {Fore.LIGHTRED_EX}GenMCShodan {Fore.LIGHTYELLOW_EX}] {Fore.LIGHTBLUE_EX}» Результат сохранен в {Fore.LIGHTGREEN_EX}{RESULT_FILE}")

# Точка входа для выполнения скрипта
if __name__ == '__main__':
    asyncio.run(main())
