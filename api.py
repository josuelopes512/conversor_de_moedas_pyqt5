import requests
import xmltodict


class ApiConversor:
    def __init__(self):
        self.api = "https://economia.awesomeapi.com.br"
    
    def moeda(self, moeda_consulta, moeda_local):
        req = requests.get(f"{self.api}/json/all/{moeda_consulta}-{moeda_local}")
        if(req.status_code == 200):
            return ((req.json()).get(moeda_consulta, None)).get("high", None)
    
    def conversor(self, moeda_consulta, moeda_local, valor):
        if moeda_local != moeda_consulta:
            if type(valor) != float:
                valor = float(valor)
                return "{:.2f}".format((valor * float(self.moeda(moeda_consulta, moeda_local))))
        return "Moeda Inválida"
    
    def get_todas_as_moedas(self):
        req = requests.get(f"{self.api}/xml/available/uniq")
        if(req.status_code == 200):
            xparse = xmltodict.parse(req.text)
            json_ = xparse.get("xml", None)
            return [i for i, _ in json_.items()]
    
    def key_to_value(self, key):
        req = requests.get(f"{self.api}/xml/available/uniq")
        if(req.status_code == 200):
            xparse = xmltodict.parse(req.text)
            json_ = xparse.get("xml", None)
            return json_.get(key, None)

de = "BRL"
para = "USD"
valor = 12

moeda = ApiConversor()
# total = moeda.conversor(de, para, 12)
# print(f"{valor} {de} = {total} {para}")
print(moeda.get_todas_as_moedas())
print(moeda.key_to_value("BRL"))