from dateutil.relativedelta import relativedelta
from datetime import datetime
import requests

plan_dict = {
    'Mensal': 1,
    'Trimestral': 3,
    'Semestral': 6,
    'Anual': 12,
}

def lookup_cep(cep):
    url = f"https://viacep.p.rapidapi.com/{cep}/json"

    headers = {
        "X-RapidAPI-Key": "d7f63ef35emsh6d3cefe0266796bp1289a7jsn0d7c44fd7122",
        "X-RapidAPI-Host": "viacep.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    return response.json()

def getDate():
    date = datetime.now()
    return date.date()

def onlyNum(string):
    num = ""
    for i in string:
        if i.isdigit():
            num += i
    
    return num

def formatCEP(string):
    return string[:5] + '-' + string[5:]

def formatPhone(string):
    return '(' + string[:2] + ') ' + string[2:7] + '-' + string[7:]

def formatCPF(string):
    return "{}{}{}.{}{}{}.{}{}{}-{}{}".format(*string)

# current_date = getDueDate('Mensal')
# print(current_date)

'''

cep
logradouro
bairro
localidade
uf - estado

'''
