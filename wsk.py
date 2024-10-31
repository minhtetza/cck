from telegram.ext import CommandHandler, Updater

AUTHORIZED_IDS = [6191863486]

def get_bot_token():
    with open('FILES/config.txt', encoding='UTF-8') as file:
        return file.read().splitlines()[2]

def wsk(update, context):
    user_id = int(update.effective_user.id) # Convert the user ID to an integer

    if user_id not in AUTHORIZED_IDS:
        update.message.reply_text('USER NOT AUTHORIZED')
        return


    new_sk = ' '.join(context.args)
    if new_sk.startswith('sk_live_'):
        try:
            with open('FILES/sk.txt', 'w') as file:
                file.write(new_sk)
            update.message.reply_text(f'SUCCESSFULLY UPDATED THE SK ✅\n\nUPDATED SK: {new_sk}\n\nThanks For Your Contribution 🥰')
        except Exception as e:
            with open("error_logs.txt", "a") as f:
                f.write(f"{e}\n")
            update.message.reply_text(f'An error occurred: {e}')
    else:
        update.message.reply_text(f'INVALID SK FORMAT.\nSUPPORTED FORMAT SK_LIVE_')

def main():
    try:
        token = get_bot_token()
        updater = Updater(token=token, use_context=True)
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('wsk', wsk))
        updater.start_polling()
        updater.idle()
    except Exception as e:
        error_message = f"An error occurred in main: {str(e)}"
        print(error_message)
        logging.error(error_message)
        traceback.print_exc()

if __name__ == '__main__':
    main()