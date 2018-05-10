from collections import defaultdict

def check_space(a):
    if a == ' ':
        return 0
    return ord(a) - 64


def belasso_encrypt(plain, kw):
    alph = defaultdict(int)
    alph[0] = ' '
    for i in range(65, 91):
        alph[i - 64] = chr(i)

    text = str.upper(plain)
    kword = str.upper(kw)
    ltx = len(text)
    lkw = len(kword)
    
    # adaptam lungimea keywordului la lungimea plaintextului
    kwadapt = kword * (int(ltx/lkw)) + kword[:int(ltx % lkw)]

    cripted = ''
    for i in range(len(kwadapt)):
        cripted += alph[(check_space(text[i]) + check_space(kwadapt[i])) % 27]

    return cripted


def belasso_decrypt(cipher, kw):

    alph = defaultdict(int)
    alph[0] = ' '
    for i in range(65, 91):
        alph[i - 64] = chr(i)

    text = str.upper(cipher)
    kword = str.upper(kw)
    ltx = len(text)
    lkw = len(kword)

    kwadapt = kword * (int(ltx/lkw)) + kword[:int(ltx % lkw)]

    decrypted = ''.join([alph[(check_space(text[i]) - check_space(kwadapt[i])) % 27] for i in range(len(kwadapt))])

    return decrypted
