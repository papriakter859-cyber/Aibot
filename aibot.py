import telebot
from telebot import types

# আপনার দেওয়া এপিআই টোকেনটি এখানে বসানো হয়েছে
API_TOKEN = '8897266210:AAE2t0ormwhqgnfYEOMimI4fTAAyHy2yrWI'

bot = telebot.TeleBot(API_TOKEN)

# কেউ /start কমান্ড দিলে এই বাটনগুলো দেখাবে
@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    
    btn1 = types.KeyboardButton('🖼️ Chart Analyzer')
    btn2 = types.KeyboardButton('🔮 Future Signals')
    btn3 = types.KeyboardButton('🔴 Live Signals')
    btn4 = types.KeyboardButton('📊 Market Sentiment')
    btn5 = types.KeyboardButton('🚀 BUG Signals')
    
    markup.row(btn1)         
    markup.row(btn2, btn3)   
    markup.row(btn4)         
    markup.row(btn5)         
    
    welcome_text = "Welcome! Let's make your trading smarter, faster & more profitable! 🚀"
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup)

# বাটনে ক্লিক করলে কি উত্তর আসবে তা হ্যান্ডেল করার কোড
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    if message.text == '🖼️ Chart Analyzer':
        bot.reply_to(message, "Analyzing the charts... Please wait! 📈")
    elif message.text == '🔮 Future Signals':
        bot.reply_to(message, "Fetching active Future Signals... 🔮")
    elif message.text == '🔴 Live Signals':
        bot.reply_to(message, "USD/ARS 1-Minute Downtrend Entry Suggestion 🔴")
    elif message.text == '📊 Market Sentiment':
        bot.reply_to(message, "Current Market Sentiment: Bullish 🐂")
    elif message.text == '🚀 BUG Signals':
        bot.reply_to(message, "Checking VIP BUG Signals... 🚀")

# বটটি সবসময় চালু রাখার জন্য
print("Bot is running...")
bot.infinity_polling()
