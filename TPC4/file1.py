import re
import json

ficheiro = open("dicionario_medico.xml", encoding="utf-8")
text = ficheiro.read()

def limpa(text):
    text = re.sub(r"\s+", " ", text)
    return text.strip() 

text = re.sub(r"</?page.*>", "", text)
text = re.sub(r"</?text.*?>", "", text) 
lista = re.findall(r"<b>(.*)</b>([^<]*)", text) 
lista = [(designacao, limpa(descricao)) for designacao, descricao in lista]

dicionario = dict(lista) 

out = open ("dicionario_medico_aula.json", "w", encoding="utf-8")
json.dump(dicionario, out, ensure_ascii=False, indent=4)
out.close()
