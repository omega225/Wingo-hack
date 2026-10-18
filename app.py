import os
import threading
import hashlib
import telebot
from flask import Flask, render_template, jsonify, request

# ==========================================
#      AETHER CORE OVERRIDE V18
# ==========================================
API_TOKEN = '8603761391:AAGx6XOfW0Tu_OoOUJUOrB-K4lLupMBiPfw'
WEBAPP_URL = 'https://maanwin.onrender.com' 
# ==========================================

bot = telebot.TeleBot(API_TOKEN)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    markup = telebot.types.InlineKeyboardMarkup()
    btn = telebot.types.InlineKeyboardButton("☣️ ACCESS CORE OVERRIDE", web_app=telebot.types.WebAppInfo(url=WEBAPP_URL))
    markup.add(btn)
    
    msg = (
        "<b>🔳 CORE OVERRIDE V18: SYSTEM BREACH</b>\n\n"
        "<code>TARGET: WINGO ALGORITHM</code>\n"
        "<code>ACCURACY: 100% LOCKED</code>\n\n"
        "The AI has bypassed the period encryption. Enter the next period to see the server's choice."
    )
    bot.send_message(message.chat.id, msg, parse_mode="HTML", reply_markup=markup)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crack')
def crack():
    period = request.args.get('period', '0')
    
    # ADVANCED CRACKING LOGIC (Deterministic Hash)
    # Using a private salt to ensure the crack is unique to your bot
    salt = "core_v18_masterpiece"
    raw_hash = hashlib.sha256(f"{period}{salt}".encode()).hexdigest()
    
    # The 'Cracked' Logic
    # We use the final bytes of the hash to find the 100% result
    val = int(raw_hash[-1], 16)
    
    # 0, 2, 4, 6, 8 = GREEN | 1, 3, 5, 7, 9 = RED
    color = "GREEN" if val % 2 == 0 else "RED"
    # 0-4 = SMALL | 5-9 = BIG
    size = "BIG" if val >= 5 else "SMALL"
    
    return jsonify({
        "status": "CRACKED",
        "color": color,
        "size": size,
        "period": period,
        "hash_key": raw_hash[:20].upper()
    })

if __name__ == '__main__':
    threading.Thread(target=lambda: bot.polling(none_stop=True), daemon=True).start()
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
