import math

def cifrazione(messaggio, chiave):
    res = ""
    cols = len(chiave)
    rows = int(math.ceil(len(messaggio) / cols))
    messaggio = messaggio + (" " * ((cols * rows) - len(messaggio)))
    table = [list(messaggio)[i: i + cols] 
              for i in range(0, len(messaggio), cols)]
    keys_order = sorted([(ch,i) for i,ch in enumerate(chiave)])
    for key in keys_order:
        for row in range(rows):
            letter = table[row][key[1]]
            res = res + "*" if letter == " " else res + letter
    return res

def decifrazione(messaggio, chiave):
    cols = len(chiave)
    rows = int(math.ceil(len(messaggio) / cols))
    keys_order = sorted([(ch,i) for i,ch in enumerate(chiave)])
    table = []
    for _ in range(rows):
        table += [[None] * cols]
    letter_pos = 0
    for key in keys_order:
        for row in range(rows):
            table[row][key[1]] = " " if messaggio[letter_pos] == "*" else messaggio[letter_pos]
            letter_pos = letter_pos + 1
    return ''.join(sum(table, []))


messaggio = "Otto bit fanno un byte !1!1!1!"
cifrato = cifrazione(messaggio, "èv3rm3)")
print(cifrato)
decifrato = decifrazione(cifrato, "èv3rm3)")
print(decifrato)