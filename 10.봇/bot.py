import telepot
import os
import logging
from module import get_dir_list
from module import get_weather
from module import money_translate

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

TELEGRAM_TOKEN = "1030547663:AAHE7rJGT-w4N8RSCxHP0H-bIJA0b49_gO0"




def handler(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)

    print(msg)

    if content_type == "text":
        str_message = msg["text"]
        if str_message[0] == "/":
            args = str_message.split(" ")
            command = args[0]
            del args[0]

            # /dir c:\\test
            if command == "/dir":
                filepath = " ".join(args)
                if filepath.strip() == "":
                    bot.sendMessage(chat_id, "/dir [대상폴더] 로 입력해주세요")
                else:
                    filelist = get_dir_list(filepath)
                    bot.sendMessage(chat_id, filelist)
            elif command[0:4] == "/get":
                filepath = " ".join(args)
                if os.path.exists(filepath):
                    if command == "/getfile":
                        bot.sendDocument(chat_id, open(filepath, "rb"))
                    elif command == "/getimage":
                        bot.sendPhoto(chat_id, open(filepath, "rb"))
                    elif command == "/getaudio":
                        bot.sendAudio(chat_id, open(filepath, "rb"))
                    elif command == "/getvideo":
                        bot.sendVideo(chat_id, open(filepath, "rb"))
                else:
                    bot.sendMessage(chat_id, "파일이 존재하지 않습니다.")
            elif command == "/weather" or command =="/날씨":
                w = " ".join(args)
                weather = get_weather(w)
                bot.sendMessage(chat_id, weather)
            elif command == "/currency" or command =="/환율":
                c = " ".join(args)
                currency = money_translate(c)
                bot.sendMessage(chat_id, currency)


# https://telepot.readthedocs.io/en/latest/
bot = telepot.Bot(TELEGRAM_TOKEN)
bot.message_loop(handler, run_forever=True)
