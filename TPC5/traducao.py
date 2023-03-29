import json

with open("termos_traduzidos.txt", "r", encoding="utf-8") as file_in:
    linhas = file_in.readlines()
    traducoes = {}
    for linha in linhas:
        key, value = linha.strip().split(" @ ")
        traducoes[key] = value

with open("exemplo_teste.json", "r", encoding="utf-8") as file_in:
    dici = json.load(file_in)

new_dici = {}

for designation, description in dici.items():
    new_dici[designation] = {
        "des": description,
        "en": traducoes.get(designation,"Não tem a tradução no documento")
    }

with open("dicionario_traducao.json", "w", encoding="utf-8") as file_out:
    json.dump(new_dici, file_out, ensure_ascii=False, indent=4)
