from telegram import Bot

def send_telegram_message(bot_token, chat_id, message):
    """
    Send a message to a Telegram chat using the bot.

    Parameters:
    - bot_token (str): The Telegram bot token.
    - chat_id (str): The Telegram chat ID where the message will be sent.
    - message (str): The message to be sent.
    """
    try:
        # Create a bot
        bot = Bot(token=bot_token)

        # Send the message
        bot.send_message(chat_id=chat_id, text=message)

        print("Message sent successfully!")
    except Exception as e:
        print(f"Error sending message: {e}")

if __name__ == "__main__":
    # Replace 'YOUR_BOT_TOKEN' with your actual bot token
    bot_token = '6508474948:AAH_V8IsNIhtnmgSiV7EbWahf3P3mPU8Ioc'
    
    # Replace 'YOUR_CHAT_ID' with your actual chat ID
    chat_id = 'rhot87bot'
    
    # Replace 'Hello, Telegram!' with the message you want to send
    message = 'Hello Mate'

    # Send the Telegram message
    send_telegram_message(bot_token, chat_id, message)
