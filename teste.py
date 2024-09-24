import re


def formatar_lista_para_regex(lista):
    lista_formatada = []

    for item in lista:
        if len(item.split()) > 1 and '-' in item:
            partes = item.split(' - ')
            marca = partes[0].strip()
            submarca = partes[1].strip()
            lista_formatada.append(rf'\b(?:{marca}\s*-\s*)?{submarca}\b')
        else:
            lista_formatada.append(r'\b' + item.replace('(', '').replace(')', '') + r'\b')

    regex = r'(' + '|'.join(lista_formatada) + r')'
    return regex


def ajustar_genero_cor(cor):
    """
    Função que ajusta o gênero da cor para o masculino. Se a cor terminar em 'a', será substituída por 'o'.
    """
    if cor and cor.endswith('a'):
        return cor[:-1] + 'o'
    return cor


l1 = ['branco', 'amarelo', 'vermelho']
l2 = ['branco', 'amarelo', 'vermelho']

lista_completa = formatar_lista_para_regex(l1 + [cor[:-1] + 'a' for cor in l2])

cor_match = re.search(lista_completa, 'amarela')

print(ajustar_genero_cor(cor_match.group(1)))
