import json
import os

import pandas as pd
import requests
import time
import xlrd
from pandas.io.json import json_normalize


def parse(name: str, area: str, only_with_salary: str, experience: str, currency: str, professional_role: str,
          employment: str, schedule: str, salary: str):
    params = {
          # Текст фильтра. В имени должно быть слово "Аналитик"
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
        'per_page': 50  # Кол-во вакансий на 1 странице

    }

    req = requests.get('https://api.hh.ru/vacancies', params)

    jsonObj = pd.DataFrame(json.loads(req.content.decode()))

    writer = pd.ExcelWriter(f'{name}.xlsx', engine='xlsxwriter')

    # Write data to an excel
    jsonObj.to_excel(writer, sheet_name="Sheet1", index=False)
    # Get workbook
    workbook = writer.book
    # Get Sheet1
    worksheet = writer.sheets['Sheet1']

    # Create a chart object.
    chart = workbook.add_chart({'type': 'column'})

    # Configure the series of the chart from the dataframe data.
    chart.add_series({'values': '=Sheet1!$B$2:$B$5'})

    # Insert the chart into the worksheet
    worksheet.insert_chart('D2', chart)

    writer.close()
    req.close()
    time.sleep(0.25)


def close():
    os.close()

if __name__ == '__main__':
    print('successful')
