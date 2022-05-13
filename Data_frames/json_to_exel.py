import json
import pandas as pd

def json_to_excel(adress):
    with open(adress) as json_file:
        data = json.load(json_file)

    df = pd.DataFrame(data)
    adr = adress[:-5]
    exel = df.to_excel(f'{adr}.xlsx')
    print("Successfully")
    return adr

json_to_excel('1.json')
