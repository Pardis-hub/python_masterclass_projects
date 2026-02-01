import telebot
import requests

TOKEN = "8107241242:AAHc0fE1fXZpJ3vka-BNQSCF-yNe0LU5KH8"
CMC_API_KEY = "b82f3e4951004709bb047ed938c4c4c2"

bot = telebot.TeleBot(TOKEN)

BASE_URL = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Hello, this is a bot that gives you current " \
    "price and 24 hour changes of currencies from CoinMarketCap Website.")
     
@bot.message_handler(func=lambda m: True)
def handle_message(message):
    symbol = message.text.strip().upper()
    params = {"symbol": symbol}
    headers = {"X-CMC_PRO_API_KEY": CMC_API_KEY}

    try:
        response = requests.get(BASE_URL, headers=headers, params=params)
        data = response.json()
    except Exception as e:
        bot.reply_to(message, f"Error in receiving data from CoinMarketCap:\n{e}")
        return
    
    coins_data = data["data"].get(symbol)
    if not coins_data:
        bot.reply_to(message, "This currency was not found!")
        return

    if isinstance(coins_data, dict):
        coins_list = [coins_data]
    else:
        coins_list = coins_data

    main_coin = min(coins_list, key=lambda c: c.get("cmc_rank", float('inf')))
    quote = main_coin.get("quote", {}).get("USD", {})

    price = quote.get("price")
    percent_change_24h = quote.get("percent_change_24h")

    if price is not None and percent_change_24h is not None:
        change_24h = price * percent_change_24h / 100
        change_24h = round(change_24h, 2)
    else:
        change_24h = "N/A"

    reply = (
        f"{main_coin.get('name')} ({main_coin.get('symbol')})\n"
        f"Current Price: {round(price, 2)}$\n"
        f"Changes in 24 hours: {change_24h}$ ({round(percent_change_24h,2)}%)"
    )
    bot.reply_to(message, reply)

bot.infinity_polling()
