import requests
import time
from colorama import Fore
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, CommandHandler, Filters


TELEGRAM_BOT_TOKEN = '7105791625:AAFQO4AH2GGMSCu8F2LliDn6NKlmhTmVmeg'


COOLDOWN_TIME = 5


last_executed_time = {}

def check_card(cx):
    url = f"bot by remoxxo"  # 2update soon
    try:
        response = requests.get(url, verify=False)
        if "Live" in response.text:
            return f"LIVE - {cx} | telegram: @xancheck"
        elif "Die" in response.text:
            return f"DEAD - {cx} | telegram: @xancheck"
        elif "Unknown" in response.text:
            return f"Unknown - {cx}"
        else:
            return "Our API is overloaded, check https://t.me/xancheck for more info 🗿"
    except requests.RequestException as e:
        return f"DEAD - {cx} | {e}"

def chk(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    cx = context.args[0]

  
    current_time = time.time()
    last_time = last_executed_time.get(user_id, 0)
    if current_time - last_time < COOLDOWN_TIME:
        context.bot.send_message(chat_id=user_id, text=f"Please wait {COOLDOWN_TIME} seconds between commands.")
        return

    result = check_card(cx)
    context.bot.send_message(chat_id=user_id, text=result)

 
    last_executed_time[user_id] = current_time

def main():
    print(Fore.YELLOW + 'Please remember that due to using "3dSEC_Bypass" module, the results MAY be inaccurate but MUST NOT.')
    time.sleep(2)


    updater = Updater(TELEGRAM_BOT_TOKEN)
    dispatcher = updater.dispatcher


    dispatcher.add_handler(CommandHandler('chk', chk))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
