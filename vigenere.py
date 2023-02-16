starting = 32
final = 126
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

print(decifrazione("4CQ\QgS_\GnWQTVY]TnZZ\PoRG[VnbXYdGa]Wl_^WXT\[NVU", "maniglio"))