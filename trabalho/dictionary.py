import random

def sorteia():
    file = open("words.txt", "r")
    word = random.choice(file.readlines())
    word = word.strip("\n")
    file.close
    return word

def existe(word):
    try:
        file = open("words.txt", "r")
        word += "\n"
        if word in file.readlines(): return True
        file.close()
        return False
    except:
        return "Erro ao abrir o arquivo"
