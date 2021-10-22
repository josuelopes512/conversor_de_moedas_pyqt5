import requests
import xmltodict

def moeda(de, para):
    req = requests.get(f"https://economia.awesomeapi.com.br/json/all/{de}-{para}")
    if(req.status_code == 200):
        # result = (req.json()).get(de, None)
        return ((req.json()).get(de, None)).get("high", None)


def conversor(moeda_input, moeda_consulta, valor):
    if type(valor) != float:
        valor = float(valor)
    return str(valor * float(moeda(moeda_consulta, moeda_input)))

def todas_as_moedas():
    req = requests.get("https://economia.awesomeapi.com.br/xml/available/uniq")
    if(req.status_code == 200):
        xparse = xmltodict.parse(req.text)
        json_ = xparse.get("xml", None)
        a = [i for i, _ in json_.items()]
        return a

def key_to_value(key):
    req = requests.get("https://economia.awesomeapi.com.br/xml/available/uniq")
    if(req.status_code == 200):
        xparse = xmltodict.parse(req.text)
        json_ = xparse.get("xml", None)
        result = json_.get(key, None)
        return result

de = "BRL"
para = "USD"
valor = 12

total = conversor(de, para, 12)
print(f"{valor} {para} = {total} {de}")
# print(todas_as_moedas())
print(key_to_value("BRL"))