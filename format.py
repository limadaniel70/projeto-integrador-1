with open('RESULTADO.txt', 'rt') as f:
    texto = f.read()

texto_fmt = texto.replace('.', ' ')

with open('RESULTADO.txt', 'wt') as f:
    f.write(texto_fmt)
