import json
import re

with open("dicionario_medico_aula.json", encoding="utf-8") as difile:
    dicionario = json.load(difile)


with open ("LIVRO-Doenças-do-Aparelho-Digestivos.html", encoding="utf-8") as livro_html:
    livro_text = livro_html.read()

termos = dicionario.keys()

html_texto = ""

for linha in livro_text.splitlines():
    palavras = re.sub(r"<.+?>", " ", linha)
    l=re.findall(r"\b[\w-]+\b", palavras)
    print(l)
    for palavra in l:
        if palavra.lower() in termos:
            link = dicionario.get(palavra.lower())
            linha = re.sub(palavra, f'<a href title="{link}">{palavra}</a>',linha)
        elif palavra in termos:
            link = dicionario.get(palavra)
            linha = re.sub(palavra, f'<a href title="{link}">{palavra}</a>',linha)
    html_texto += linha + "\n"

with open("LIVRO-Doenças-do-Aparelho-Digestivos.html","w", encoding="utf-8") as file_html:
    file_html.write(html_texto)
