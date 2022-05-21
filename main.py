# THIS`IS TELEGRAM_BOT
import json
import logging
import pandas as pd
import xlsxwriter
import xlrd
import sqlite3
from db import BotDB

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import AndroidVacance
import IOSVacance
import todaysVacacies
from config import TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN)

dp = Dispatcher(bot)
# connect the bot db
BotDB = BotDB('data.db')


@dp.message_handler(commands=['start'])
async def welcomeMessages(message: types.Message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton('Хабарландыруларды қарау')
    item2 = types.KeyboardButton('Парсинг')
    markup.add(item1, item2)
    await message.answer("Cәлем {0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user)+str(message.from_user.id),
                         reply_markup=markup)
    if not BotDB.user_exists(str(message.from_user.id)):
        BotDB.add_user(str(message.from_user.id), str(message.from_user.first_name))
        print("authorization successfully")
        await message.answer("Қош келдіңіз!\n" +
                             "Менің қолымнан келесі істер келеді: \n" +
                             "/start - Бастау\n" +
                             "/about - Пайдаланушы нұсқаулығы\n" +
                             "/vacancies - Бос жұмыс орындарының тізімі")




@dp.message_handler(content_types=['text'])
async def bot_Messages(message: types.Message):
    if message.text == "Хабарландыруларды қарау":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Web -Бағдарламалау')
        item2 = types.KeyboardButton('Android -Бағдарламалау')
        item3 = types.KeyboardButton('IOS -Бағдарламалау')
        item4 = types.KeyboardButton('⬅ Артқа')
        markup.add(item1, item2, item3,item4)
        await message.answer("Cәлем {0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user),
                             reply_markup=markup)

    elif message.text == 'Парсинг':
        photo = open('parser.png', 'rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159p')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160p')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205p')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        if not BotDB.resume_exists(str(message.from_user.first_name)):
            BotDB.create_resume(str(message.from_user.first_name))
            print("authorization successfully")
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer("Қаланы көрсетіңіз", reply_markup=inline_kb1)

    elif message.text == 'Web -Бағдарламалау':
        photo = open("Web-Developer.jpeg", 'rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Front-end Бағдарламалау', callback_data='Front-end dev!')
        inline_btn_2 = InlineKeyboardButton('Back-end Бағдарламалау', callback_data='Back-end dev!')
        inline_btn_3 = InlineKeyboardButton('Full-stack Бағдарламалау', callback_data='Full-stack dev!')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'Web -Бағдарламалау\' бөліміндесіз! \nСенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)

    elif message.text == 'Android -Бағдарламалау':
        photo = open("android.jpeg", 'rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'Android -Бағдарламалау\' бөліміндесіз \n Сенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)

    elif message.text == 'IOS -Бағдарламалау':
        photo = open('iOS-Developer.jpg','rb')
        await message.answer_photo(photo)
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159i')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160i')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205i')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await message.answer(
            "{0.first_name}\n- сіз \'IOS -Бағдарламалау\' бөліміндесіз \n Сенің телеграм бот асистентің!".format(
                message.from_user), reply_markup=inline_kb1)

    elif message.text == '⬅ Артқа':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton('Хабарландыруларды қарау')
        item2 = types.KeyboardButton('Парсинг')
        markup.add(item1, item2)
        await message.answer(
            "{0.first_name}\nYou tap to \'⬅ Артқа\' button \n your assistant telegram bot!".format(
                message.from_user), reply_markup=markup)
        await message.delete()




@dp.message_handler(commands=['about'])
async def about(message: types.Message):
    photo = open('logo.jfif','rb')
    await message.answer_photo(photo)
    await message.answer("{0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user)
                         + "\n/about - Пайдаланушы нұсқаулығы"
                         + "\n/vacancies - Күннің 10 үздік ұсынысы!")



@dp.message_handler(commands=['vacancies'])
async def vacancies(message: types.Message):
    photo = open('logo.jfif', 'rb')
    await message.answer_photo(photo)
    inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159t')
    inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160t')
    inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205t')
    back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
    inline_kb1 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
    await message.answer("Күннің 10 үздік ұсынысы!", reply_markup=inline_kb1)

inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159t')
inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160t')
inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205t')
back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)


inline_btn_4 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159t')
inline_btn_5 = InlineKeyboardButton('Алматы қаласы', callback_data='160t')
inline_btn_6 = InlineKeyboardButton('', callback_data='')
back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
inline_kb2 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)


@dp.callback_query_handler()
async def process_callback_btn(callback_query: types.CallbackQuery):
    if callback_query.data == 'Front-end dev!':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        f = open('Front-end.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '159p':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        # f = open('Web.xlsx', 'rb')
        # await bot.send_document(callback_query.message.chat.id,f)
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), str(area))
        inline_btn_1 = InlineKeyboardButton('Нұр-Сұлтан қаласы', callback_data='159t')
        inline_btn_2 = InlineKeyboardButton('Алматы қаласы', callback_data='160t')
        inline_btn_3 = InlineKeyboardButton('Шымкент қаласы', callback_data='205t')
        back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
        inline_kb2 = InlineKeyboardMarkup().add(inline_btn_1, inline_btn_2, inline_btn_3, back)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы",reply_markup=inline_kb2)
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')


    elif callback_query.data == '205p':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), str(area))
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы")
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')


    elif callback_query.data == '160p':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), area)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы")
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')

    elif callback_query.data == '⬅ Back':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id,callback_query.message.message_id)

    elif callback_query.data == 'Back-end dev!':
        await bot.answer_callback_query(callback_query.id)
        f = open('Back-end.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == 'Full-stack dev!':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        f = open('Full-stack.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id,v['alternate_url'], parse_mode='html')

    elif callback_query.data == '159':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '205':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '160':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id,"Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        AndroidVacance.parse(int(callback_query.data))
        f = open('Android.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '159i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

    elif callback_query.data == '205i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '160i':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        IOSVacance.parse(int(callback_query.data[:-1]))
        f = open('IOS development.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '159t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '205t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

    elif callback_query.data == '160t':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы бойынша бос жұмыс орындары тізімі:")
        todaysVacacies.parse(int(callback_query.data[:-1]))
        f = open('Top10.json', encoding='utf8')
        jsonText = f.read()
        f.close()
        jsonObj = json.loads(jsonText)
        for v in jsonObj['items']:
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')


async def  json_to_excel(adress):
    json_file = open(adress, encoding='utf8')
    data = json.load(json_file)
    df = pd.DataFrame(data)
    writer = pd.ExcelWriter('data.xlsx', engine='xlsxwriter')
    df.to_excel(writer, sheet_name='Sheet1', index=False)
    writer.save()
    print("Successfully")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
