#!/usr/bin/env python3

import telebot
import datetime
import logging
import json
import glob
import os


logger = telebot.logger
logger.setLevel(logging.INFO)

TOKEN = '1454965577:AAHqSx6CXCKvXjo1PCc7BLb8z4CJlOa5M-U'
files_directory = "files"
days_left = 3

def safe_entered_date(user_name):
    if not os.path.exists(files_directory):
        os.makedirs(files_directory)

    with open(f"{files_directory}/{user_name}.json", "w") as write_file:               
        data = {
                user_name : {
                    "date" : f"{datetime.date.today()}"
                    }
            }
        json.dump(data, write_file)

data_dict = {}
def load_json_data():    
    for res in (glob.glob(f"./{files_directory}/*.json")):
        with open(res, "r") as read_file:
            data_dict.update(json.load(read_file))

bot = telebot.TeleBot(TOKEN)

# @bot.message_handler(commands=['start'])
# def start_message(message):    
#     bot.send_message(message.chat.id, '/start')

@bot.message_handler(content_types=['text'])
def send_text(message):  
    user_data = data_dict.get(message.from_user.username)     
    date_today = datetime.date.today()
    delta_days = days_left
    
    if (user_data is not None):        
        user_last_date = datetime.datetime.strptime(user_data.get("date", f"{date_today}"), '%Y-%m-%d').date()        
        delta_days = (date_today - user_last_date).days

    if delta_days < days_left:
        safe_entered_date(message.from_user.username)
    elif delta_days >= days_left:       
        if message.from_user.username == 'M_e_t_a_ll_e_r': 
            bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAKfKF_w7aQluyKbWd_GGrcIixcrpbb7AAI1AAOtZbwU9aVxXMUw5eAeBA')    
        elif message.from_user.username == 'Momos_69':
            bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=TrfgpgB4HWc')
        elif message.from_user.username == 'Pavel6410':
            bot.send_photo(message.chat.id, 'https://risovach.ru/upload/2014/11/mem/chernyj-vlastelin_66046702_orig_.jpg')

def main():
    load_json_data()        
    bot.polling(none_stop=True)
    
if __name__ == '__main__':
    main()