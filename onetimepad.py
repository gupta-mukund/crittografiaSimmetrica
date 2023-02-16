import random
starting = 32
final = 126

def generateKey(size):
    res = ""
    while (len(res) < size):
        res = res + chr(random.randint(starting, final))
    return res

def cifrazione(messaggio, chiave):
    res = ""
    chiave_pos = 0
    for single in messaggio:
        if chiave_pos == len(chiave):
            chiave_pos = 0
        code = (ord(single) - starting + ord(chiave[chiave_pos]) - starting) % (final - starting) + starting - 1
        res = res + chr(code)
        chiave_pos = chiave_pos + 1
    return res

def decifrazione(messaggio, chiave):
    res = ""
    chiave_pos = 0
    for single in messaggio:
        if chiave_pos == len(chiave):
            chiave_pos = 0
        code = (ord(single) - ord(chiave[chiave_pos]) + final - starting) % (final - starting) + starting + 1
        res = res + chr(code) 
        chiave_pos = chiave_pos + 1
    return res

messaggio = "ciaosonoio"
key = generateKey(len(messaggio))
cifrato = cifrazione(messaggio, key)
print(cifrato)
decifrato = decifrazione(cifrato, key)
print(decifrato)