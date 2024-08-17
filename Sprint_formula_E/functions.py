import os
import time
from werkzeug.security import check_password_hash, generate_password_hash
from textwrap import wrap


def header(txt, symbol):
    gap = len(txt) * 2
    print(f"{symbol}" * gap)
    print(txt.center(gap))
    print(f"{symbol}" * gap)


def register(name, email, password):
    if not os.path.exists("database.txt"):
        file = open("database.txt", "x")
        file.close()

    file = open("database.txt", "r")
    for line in file:
        data = line.split("|")

        if data[0].strip().lower() == name.lower():
            # print("Nome de usuário já utilizado!")
            file.close()
            return False
    file.close()

    file = open("database.txt", "a")
    hash_password = generate_password_hash(password)
    file.write(f"{name:<10}|{email:<10}|{hash_password}|\n")

    file.close()
    return True


def login(name, password):
    if not os.path.exists("database.txt"):
        return False

    file = open("database.txt", "r")

    for line in file:
        data = line.split("|")

        if name.lower() == data[0].strip().lower():
            if check_password_hash(data[2], password):
                file.close()
                return True
            else:
                print("Senha Incorreta")
                file.close()
                return False

    file.close()
    print("Nome de usuário não encontrado")
    return False


def show_reports():
    if not os.path.exists("reports.txt"):
        file = open("reports.txt", "x")
        file.close()

    file = open("reports.txt", "r")

    for line in file:
        print(line, end='')

    file.close()


def report_issue(user, issue):
    file = open("reports.txt", "a")

    file.write(f"{user:<10}|'{issue}'\n")
    file.close()
    print("Problema reportado com sucesso!")


def stopwatch_minigame():
    tempo_init = time.time()
    input("\033[1;37;41mAGORA: \033[m")
    tempo_final = time.time()

    tempo = tempo_final - tempo_init

    return tempo


def ai_str_format(text, len_wrap):
    # TODO: Formatar bullet points
    for old, new in [
        ("* ", "\n• "),
        ("**", "")
    ]:
        texto = text.replace(old, new)
    texto = wrap(texto, width=len_wrap)

    for linha in texto:
        for char in linha:
            print(char, end='')
            time.sleep(0.03)
        print()
