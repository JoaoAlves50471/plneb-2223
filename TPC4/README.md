Resolução do exercício começado na aula em que se pretendia criar um ficheiro html do livro de doenças do aparelho digestivo em que ao passar com o rato nas palavras cuja presença estava tanto no livro como no dicionário médico (que foi passado a um ficheiro json) apresentasse as definições das palavras.

No final não consegui testar com o ficheiro completo visto que apresentava: Traceback (most recent call last): File "c:\Users\Hp\Desktop\4º Ano\plneb-2223\plneb-2223\TPC4\file2.py", line 20, in <module>
    linha = re.sub(palavra, f'<a href="{link}" title="{palavra}">{palavra}</a>',linha)
  File "C:\Program Files\Python310\lib\re.py", line 209, in sub
    return _compile(pattern, flags).sub(repl, string, count)
MemoryError

Contudo era de se prever que este funcionasse caso o ficheiro fosse mais reduzido.