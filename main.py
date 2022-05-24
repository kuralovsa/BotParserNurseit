# THIS`IS TELEGRAM_BOT
import json
import logging
import pandas as pd
import asyncio

import Parser
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
    await message.answer(
        "Cәлем {0.first_name}\n Сенің телеграм бот асистентің!".format(message.from_user),
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
        markup.add(item1, item2, item3, item4)
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
        photo = open('iOS-Developer.jpg', 'rb')
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
    photo = open('logo.jfif', 'rb')
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

inline_btn_4 = InlineKeyboardButton('Әзірлеуші', callback_data='96')
inline_btn_5 = InlineKeyboardButton('Аналитик', callback_data='10')
inline_btn_6 = InlineKeyboardButton('Дизайнер', callback_data='34')
inline_btn_7 = InlineKeyboardButton('Жүйелік администратор', callback_data='96')
inline_btn_8 = InlineKeyboardButton('Oйын әзірлеушісі', callback_data='25')
inline_btn_9 = InlineKeyboardButton('Тестировщик', callback_data='124')
inline_btn_10 = InlineKeyboardButton('Жүйе инженері', callback_data='114')
inline_btn_11 = InlineKeyboardButton('Техникалық директор', callback_data='125')
back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
inline_kb3 = InlineKeyboardMarkup().add(inline_btn_4, inline_btn_5, inline_btn_6, inline_btn_7, inline_btn_8,
                                        inline_btn_9, inline_btn_10, inline_btn_11, back)

inline_btn_12 = InlineKeyboardButton('100000tg', callback_data='100000')
inline_btn_13 = InlineKeyboardButton('200000tg', callback_data='200000')
inline_btn14 = InlineKeyboardButton('300000tg', callback_data='300000')
back = InlineKeyboardButton('⬅ Back', callback_data='⬅ Back')
inline_salarykb = InlineKeyboardMarkup().add(inline_btn_12, inline_btn_13, inline_btn14, back)

inline_btn15 = InlineKeyboardButton('Тәжірибе жоқ ', callback_data='noExperience')
inline_btn16 = InlineKeyboardButton('1 жылдан 3 жылға дейін', callback_data='between1And3')
inline_btn17 = InlineKeyboardButton('3-дан 6 дейін жыл ', callback_data='between3And6')
inline_btn18 = InlineKeyboardButton('6-дан артық жыл', callback_data='moreThan6')
inline_btn19 = InlineKeyboardButton('Мaғынасы жоқ', callback_data='false')
inline_exp_kb = InlineKeyboardMarkup().add(inline_btn15, inline_btn16, inline_btn17, inline_btn18, inline_btn19, back)

inline_btn20 = InlineKeyboardButton('Толық жұмысбастылық ', callback_data='full')
inline_btn21 = InlineKeyboardButton('Жартылай жұмысбастылық', callback_data='part')
inline_btn22 = InlineKeyboardButton('Тағылымдама ', callback_data='probation')
inline_btn24 = InlineKeyboardButton('Жобалық жұмыс', callback_data='project')
inline_btn23 = InlineKeyboardButton('Мaғынасы жоқ', callback_data='false')
inline_emp_kb = InlineKeyboardMarkup().add(inline_btn20, inline_btn21, inline_btn22, inline_btn24, inline_btn23, back)

inline_btn25 = InlineKeyboardButton('Толық күн ', callback_data='fullDay')
inline_btn26 = InlineKeyboardButton('Икемді кесте', callback_data='flexible')
inline_btn27 = InlineKeyboardButton('Қашақтақтан жұмыс ', callback_data='remote')
inline_btn28 = InlineKeyboardButton('Вахталық әдіс', callback_data='flyInFlyOut')
inline_btn33 = InlineKeyboardButton('Ауысымды кесте', callback_data='shift')
inline_btn29 = InlineKeyboardButton('Мaғынасы жоқ', callback_data='false')
inline_sce_kb = InlineKeyboardMarkup().add(inline_btn25, inline_btn26, inline_btn27, inline_btn28, inline_btn33, inline_btn29, back)

inline_btn30 = InlineKeyboardButton('Результатты алу', callback_data='result')
inline_btn31 = InlineKeyboardButton('Резюмеге шолу', callback_data='resume')
get_result = InlineKeyboardMarkup().add(inline_btn30, inline_btn31)

prof_roles = ['96', '10', '34', '96', '25', '124', '114', '125']
salary = ['100000', '200000', '300000']
experience = ['noExperience', 'between1And3', 'between3And6', 'moreThan6', 'false']
employment = ['full', 'part', 'probation', 'project', 'false']
schedule = ['fullDay', 'flexible', 'remote', 'flyInFlyOut', 'shift', 'false']
results = ['resume', 'result']


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
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), str(area))
        await bot.send_message(callback_query.message.chat.id, "Нұр-Сұлтан қаласы")
        await bot.send_message(callback_query.message.chat.id, "Кәсіби аймақ", reply_markup=inline_kb3)
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')


    elif callback_query.data == '205p':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), str(area))
        await bot.send_message(callback_query.message.chat.id, "Шымкент қаласы")
        await bot.send_message(callback_query.message.chat.id, "Кәсіби аймақ", reply_markup=inline_kb3)
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')


    elif callback_query.data == '160p':
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        area = callback_query.data[:-1]
        BotDB.set_city(str(callback_query.from_user.first_name), area)
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы")
        await bot.send_message(callback_query.message.chat.id, "Кәсіби аймақ", reply_markup=inline_kb3)
        print(f'For {callback_query.from_user.first_name} - added area value{area}!!!')

    elif prof_role(callback_query.data, prof_roles):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        BotDB.set_spesiolization(str(callback_query.from_user.first_name), str(callback_query.data))
        await bot.send_message(callback_query.message.chat.id, "Жалақы соммасы:", reply_markup=inline_salarykb)
        print('successful role')
        callback_query.clean()

    elif prof_salary(callback_query.data, salary):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        BotDB.set_salary(str(callback_query.from_user.first_name), str(callback_query.data))
        await bot.send_message(callback_query.message.chat.id, "Жұмыс тәжірибесі :", reply_markup=inline_exp_kb)
        callback_query.clean()

    elif prof_exp(callback_query.data, experience):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        BotDB.set_experience(str(callback_query.from_user.first_name), str(callback_query.data))
        await bot.send_message(callback_query.message.chat.id, "Жұмысбастылық түрі :", reply_markup=inline_emp_kb)
        callback_query.clean()

    elif prof_employment(callback_query.data, employment):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        BotDB.set_employment(str(callback_query.from_user.first_name), str(callback_query.data))
        await bot.send_message(callback_query.message.chat.id, "Жұмыс кестесі :", reply_markup=inline_sce_kb)
        callback_query.clean()

    elif prof_schedule(callback_query.data, schedule):
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)
        BotDB.set_schedule(str(callback_query.from_user.first_name), str(callback_query.data))
        await bot.send_message(callback_query.message.chat.id, "Жұмысорнының атауы :", reply_markup=get_result)
        callback_query.clean()

    elif get_result_resum(callback_query.data, results):
        data = BotDB.get_resume(callback_query.from_user.first_name)
        data = list(data)
        data = data[0]
        Parser.parse(name=data[0], area=data[1], only_with_salary='true', experience=data[4], currency='KZT',
                     professional_role=data[2], employment=data[5], salary=data[3], schedule=data[6])
        if str(callback_query.data) == 'resume':
            await bot.send_message(callback_query.message.chat.id, f'Есіміңіз: {data[0]}\nЖұмыс іздеу аймағы :{data[1]}\nКәсіби аймақ: {data[2]}\nЖалақы соммасы: {data[3]}\nЖұмыс тәжірибесі : {data[4]}\nЖұмысбастылық түрі : {data[5]}\nЖұмыс кестесі : {data[6]}')
            print(data)
        elif str(callback_query.data) == 'result':
            f = open(f'{data[0]}.xlsx', 'rb')
            await bot.send_message(callback_query.message.chat.id, 'Сіздің іздеген ақпараттар дайын!')
            await bot.send_document(callback_query.message.chat.id, document=f)

    elif callback_query.data == '⬅ Back':
        await bot.answer_callback_query(callback_query.id)
        await bot.delete_message(callback_query.message.chat.id, callback_query.message.message_id)

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
            await bot.send_message(callback_query.message.chat.id, v['alternate_url'], parse_mode='html')

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
        await bot.send_message(callback_query.message.chat.id, "Алматы қаласы бойынша бос жұмыс орындары тізімі:")
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


def prof_role(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


def prof_salary(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


def prof_exp(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


def prof_employment(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


def prof_schedule(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


def get_result_resum(call_data, enum_date):
    e = enum_date
    for i in range(len(e)):
        if e[i] == str(call_data):
            return True


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
