import json
import requests
import time


def parse(name: str, area: int, only_with_salary: str, experience: str, currency: str, professional_role: str, employment: str, schedule: str,salary: str):
    params = {
        'text': name,  # Текст фильтра. В имени должно быть слово "Аналитик"
        'area': area,  # Поиск ощуществляется по вакансиям города area
        'only_with_salary': only_with_salary,
        'professional_role': professional_role,
        'currency': currency,
        'schedule': schedule,
        'employment': employment,
        'experience': experience,
        'salary': salary,
        'locale': 'KZ',
        'language': 'kz',
        'host': 'hh.kz',
        'page': 0,  # Индекс страницы поиска на HH
        'per_page': 30  # Кол-во вакансий на 1 странице

    }

    req = requests.get('https://api.hh.ru/vacancies', params)
    jsonObj = json.loads(req.content.decode())

    nextFileName = 'Parse.json'

    f = open(nextFileName, mode='w', encoding='utf8')
    f.write(json.dumps(jsonObj, ensure_ascii=False))
    f.close()
    req.close()
    time.sleep(0.25)

parse(name='Web',area=159,only_with_salary='true',experience='between1And3',currency='KZT',professional_role='96',employment='full',schedule='fullDay',salary='100000')
print("Parsing successfully")