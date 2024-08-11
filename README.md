# GenMCShodan
is a Python utility for scanning and gathering information about Minecraft servers using the Shodan API, providing insights into server status, player counts, and configurations.

# EN
**GenMCShodan** is a Python-based tool designed to scan and retrieve information about Minecraft servers using the Shodan API. This tool is particularly useful for network administrators and security enthusiasts interested in analyzing Minecraft server infrastructure.

## Features
- **Shodan API Integration**: Leverages Shodan's vast database to find Minecraft servers.
- **Minecraft Server Status**: Retrieves server status including player count, server version, and MOTD.
- **Colorful CLI Output**: Uses colorama for a visually appealing command-line interface.
- **Result Logging**: Saves scan results to a specified file for further analysis.

## Prerequisites
- **Python 3.x**: Make sure Python is installed on your system.
- **Shodan API Key**: You need a valid Shodan API key to use this tool.

## Installation
1. Clone the repository:
```bash
git clone https://github.com/geniuszlyy/GenMCShodan.git
```
2. Navigate to the project directory:
```bash
cd GenMCShodan
```
3. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## Usage
1. **Setup API Key**: Create a `config.json` file in the root directory with your Shodan API key.
```bash
{
    "SHODAN_API_KEY": "your_api_key_here"
}
```
2. **Run the Tool**:
```bash
python GenMCShodan.py [PORT] [RESULT_FILE_PATH] [SEARCH_QUERY]
```
- **PORT**: The port to scan (e.g., 25565 for Minecraft).
- **RESULT_FILE_PATH**: Path to save the scan results.
- **SEARCH_QUERY**: The Shodan search query to find servers.

![image](https://github.com/user-attachments/assets/304cbd9e-c3c0-4b7f-b8a0-9cfcdb0b7421)


## Example
```bash
python GenMCShodan.py 25565 results.txt "Minecraft"
```
![image](https://github.com/user-attachments/assets/c6247038-87ec-433b-bd99-70c2fa9f3cd2)

![image](https://github.com/user-attachments/assets/331b4e7c-b87e-4752-8509-d4fff61cb024)



# RU
**GenMCShodan** — это инструмент на Python, предназначенный для сканирования и получения информации о серверах Minecraft с использованием API Shodan. Этот инструмент особенно полезен для сетевых администраторов и энтузиастов безопасности, интересующихся анализом инфраструктуры серверов Minecraft.

## Особенности
- **Интеграция с Shodan API**: Использует обширную базу данных Shodan для поиска серверов Minecraft.
- **Статус сервера Minecraft**: Получает статус сервера, включая количество игроков, версию сервера и MOTD.
- **Красочный CLI вывод**: Использует colorama для визуально привлекательного интерфейса командной строки.
- **Логирование результатов**: Сохраняет результаты сканирования в указанный файл для дальнейшего анализа.

## Требования
- **Python 3.x**: Убедитесь, что Python установлен на вашем компьютере.
- **Shodan API ключ**: Вам нужен действующий API ключ Shodan для использования этого инструмента.

## Установка
1. Клонируйте репозиторий:
```bash
git clone https://github.com/geniuszlyy/GenMCShodan.git
```
2. Перейдите в директорию проекта:
```bash
cd GenMCShodan
```
3. Установите необходимые пакеты Python:
```bash
pip install -r requirements.txt
```

## Использование
1. **Настройка API ключа**: Создайте файл `config.json` в корневой директории с вашим API ключом Shodan.
```bash
{
    "SHODAN_API_KEY": "your_api_key_here"
}
```
2. **Запуск инструмента**:
```bash
python GenMCShodan.py [PORT] [RESULT_FILE_PATH] [SEARCH_QUERY]
```
- **PORT**: Порт для сканирования (например, 25565 для Minecraft).
- **RESULT_FILE_PATH**: Путь для сохранения результатов сканирования.
- **SEARCH_QUERY**: Поисковый запрос для Shodan.

![image](https://github.com/user-attachments/assets/304cbd9e-c3c0-4b7f-b8a0-9cfcdb0b7421)

## Пример
```bash
python GenMCShodan.py 25565 results.txt "Minecraft"
```
![image](https://github.com/user-attachments/assets/c6247038-87ec-433b-bd99-70c2fa9f3cd2)

![image](https://github.com/user-attachments/assets/331b4e7c-b87e-4752-8509-d4fff61cb024)
