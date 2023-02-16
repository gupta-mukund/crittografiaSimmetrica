import math

def cifrazione(messaggio, chiave):
    res = ""
    cols = len(chiave)
    rows = int(math.ceil(len(messaggio) / cols))
    messaggio = messaggio + (" " * ((cols * rows) - len(messaggio)))
    # messaggio = re.sub(r"^\s+|\s+$", "_", messaggio, flags=re.MULTILINE)
    #table = [[messaggio[mess_pos]] * cols for i in range(rows)]
    table = [list(messaggio)[i: i + cols] 
              for i in range(0, len(messaggio), cols)]
    keys_order = sorted([(ch,i) for i,ch in enumerate(chiave)])
    for key in keys_order:
        for row in range(rows):
            letter = table[row][key[1]]
            res = res + "_" if letter == " " else res + letter
    return res

def decifrazione(messaggio, chiave):
    res = ""
    cols = len(chiave)
    rows = int(math.ceil(len(messaggio) / cols))
    keys_order = sorted([(ch,i) for i,ch in enumerate(chiave)])
    table = []
    for _ in range(rows):
        table += [[None] * cols]
    letter_pos = 0
    for key in keys_order:
        for row in range(rows):
            table[row][key[1]] = " " if messaggio[letter_pos] == "_" else messaggio[letter_pos]
            letter_pos = letter_pos + 1
    return ''.join(sum(table, []))


# cifrazione("Geeks for Geeks", "HACK")
decifrazione("angusri*C_i,oMoiadoi.i*omo_a_gioiog*si_nmfl*sagbepn?", "LOvISoN")

chiave = "LOvISoN"
keys_order = sorted([(ch,i) for i,ch in enumerate(chiave)])
print(keys_order)

# print(sorted(chiave))