import socket
import asyncio
import telegram

ip_address = "IP_ADRESS"
port = 22
bot_token = "Telegram_TOKEN"
chat_id = "CHAT_ID"

bot = telegram.Bot(token=bot_token)

async def check_server():
    server_down = False  # флаг-счетчик

    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)

        try:
            s.connect((ip_address, port))
            print("Сервер доступен")
            if server_down:
                await bot.send_message(chat_id=chat_id, text="Сервер снова доступен")
            server_down = False
        except:
            print("Сервер_Макаров недоступен")
            if not server_down:
                await bot.send_message(chat_id=chat_id, text="Сервер Макаров недоступен")
            server_down = True

        s.close()
        await asyncio.sleep(60)  # ждем 60 секунд перед следующей проверкой

async def main():
    await check_server()

if __name__ == "__main__":
    asyncio.run(main())
