import requests
import xmltodict

class ApiConversor:
    def __init__(self):
        self.api = "https://economia.awesomeapi.com.br"
        self.keys = self.get_keys()
        self.todas_as_moedas = sorted([i for i, _ in self.keys.items()])
        self.carrega_combinacoes = self.essas_combinacoes()
        self.moeda_consulta = ""
        self.moeda_local = ""

    def essas_combinacoes(self):
        dic = {}
        req = requests.get(f"{self.api}/json/available")
        if(req.status_code == 200):
            combinacoes = sorted([i for i, _ in req.json().items()])
            for j in combinacoes:
                a = j.split("-")
                if a[0] not in dic:
                    dic.update({a[0]:[]})
                    dic[a[0]].append(a[1])
                else:
                    dic[a[0]].append(a[1])
            return dic

    def is_possui_combinacao(self):
        result = self.carrega_combinacoes.get(self.moeda_consulta, None)
        return(True if self.moeda_local in result else None)

    def moeda(self):
        req = requests.get(f"{self.api}/json/all/{self.moeda_consulta}-{self.moeda_local}")
        if(req.status_code == 200):
            return "{:.2f}".format(float(((req.json()).get(self.moeda_consulta, None)).get("high", None)))

    def conversor(self, moeda_consulta, moeda_local, valor):
        self.moeda_consulta = moeda_consulta
        self.moeda_local = moeda_local

        if moeda_local != moeda_consulta and self.is_possui_combinacao():
            moeda = self.moeda()
            if type(valor) != float:
                valor = float(valor)
                return "{:.2f}".format((valor * float(moeda)))
            else:
                total = "{:.2f}".format(valor * float(moeda))
                return total
        if not self.is_possui_combinacao():
            return "Não Disponivel"

        return "Moeda Inválida"
    
    def get_keys(self):
        req = requests.get(f"{self.api}/xml/available/uniq")
        if(req.status_code == 200):
            xparse = xmltodict.parse(req.text)
            json_ = xparse.get("xml", None)
            return json_
    
    def key_to_value(self, key):
        return self.keys[key]