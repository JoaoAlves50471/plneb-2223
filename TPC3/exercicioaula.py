import re

file = open ('dicionario_medico.txt', encoding='utf8')
text = file.read()
text = re.sub(r'\f','\n', text)
text = re.sub(r'(\n\n.+)\n\n',r'\1',text)

entries = re.findall(r'\n\n(.+)((?:\n.+)+)', text)

new_entries = [(designation, description.strip()) for designation, description in entries]

file.close()

html = open('dicionario_medico.html', 'w', encoding = 'utf8')

header = '''<html>
<head>
    <meta charset="UTF-8">
    <title>Dicionário Médico</title>
    <style>
        body {
            background-image: url('https://img.freepik.com/free-vector/medical-healthcare-blue-color_1017-26807.jpg');
            background-color: #F5F5F5;
            font-family: Arial, sans-serif;
            font-size: 16px;
            color: #333;
        }

        h1 {
            margin-top: 30px;
            text-align: center;
            font-size: 36px;
            color: #002285;
        }

        table {
            margin: 0 auto;
            border-collapse: collapse;
            width: 80%;
            max-width: 800px;
        }

        th {
            background-color: #0088CB;
            color: #fff;
            font-size: 20px;
            font-weight: normal;
            text-align: center;
            padding: 15px;
            border: 1px solid #ddd;
        }

        td {
            background-color: #fff;
            color: #333;
            font-size: 16px;
            text-align: left;
            padding: 15px;
            border: 1px solid #ddd;
        }

        tr:nth-child(even) td {
            background-color: #F5F5F5;
        }
    </style>
</head>
<body>
    <h1>Dicionário Médico</h1>
'''

body = '<table>\n'
body += '\t<thead>\n'
body += '\t\t<tr>\n'
body += '\t\t\t<th>Designação</th>\n'
body += '\t\t\t<th>Descrição</th>\n'
body += '\t\t</tr>\n'
body += '\t</thead>\n'
body += '\t<tbody>\n'
for designation, description in new_entries:
    body += '\t\t<tr>\n'
    body += '\t\t\t<td><b>' + designation + '</b></td>\n'
    body += '\t\t\t<td>' + description + '</td>\n'
    body += '\t\t</tr>\n'
body += '\t</tbody>\n'
body += '</table>\n'

footer = '''</body>
</html>'''

html.write(header + body + footer)
html.close()