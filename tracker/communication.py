import telegram

import settings

class Communication:
    
    def __init__(self, item_name, item_url, item_price, target_price):
        self.item_name = item_name
        self.item_url = item_url
        self.item_price = item_price
        self.target_price = target_price
        
    def send_telegram(self):
        bot = telegram.Bot(token=settings.TELEGRAM_TOKEN)
        bot.sendMessage(chat_id=settings.CHAT_ID, text=f'📉📉 {self.item_name} ha bajado de precio a {self.item_price}!')
