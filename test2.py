import socket
import asyncio
import telegram

servers = [
    {"address": "37.53.83.166", "port": 22, "name": "Сервер_makariv"},
    {"address": "176.104.12.189", "port": 22, "name": "Сервер_kiev"},
    {"address": "213.246.39.44", "port": 22, "name": "Test_ex1arey"},
    {"address": "109.238.14.118", "port": 22, "name": "Test_annet"}
]

bot_token = "6152656052:AAHXWdYKO6dC1484ugHZa7fbehw9KiDzR3c"
chat_id = "413839778"

bot = telegram.Bot(token=bot_token)

async def check_servers():
    server_down = {server["name"]: False for server in servers}
    server_retry_count = {server["name"]: 0 for server in servers}

    while True:
        for server in servers:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(2)

            try:
                s.connect((server["address"], server["port"]))
                print(f"{server['name']} доступен")
                if server_down[server["name"]]:
                    await bot.send_message(chat_id=chat_id, text=f"{server['name']} снова доступен")
                server_down[server["name"]] = False
                server_retry_count[server["name"]] = 0
            except:
                print(f"{server['name']} недоступен")
                server_retry_count[server["name"]] += 1
                if server_retry_count[server["name"]] >= 3 and not server_down[server["name"]]:
                    await bot.send_message(chat_id=chat_id, text=f"{server['name']} недоступен")
                    server_down[server["name"]] = True
                    server_retry_count[server["name"]] = 0

            s.close()

        await asyncio.sleep(60)

async def main():
    await check_servers()

if __name__ == "__main__":
    asyncio.run(main())
