import socket
import asyncio
import telegram

servers = [
    {"address": "IP ADRESS", "port": 22, "name": "Название сервера"},
    {"address": "IP ADRESS", "port": 22, "name": "Название сервера"},
    {"address": "IP ADRESS", "port": 22, "name": "Название сервера"},
    {"address": "IP ADRESS", "port": 22, "name": "Название сервера"}
]

bot_token = "Telegram TOKEN"
chat_id = "CHAT ID"

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
