# Coder par Waz Yassine 03-06-2022
# Epreuve pratique AlgoSI 2022 (Nouveau régime)

def Saisie():
    Test = False
    while not Test:
        code = input("Donner un code de recherge composé de 13 chiffres : ")
        Test = len(code) == 13 and code.isnumeric()
    return code

def Premier(ch):
    n = int(ch)
    i = 2
    while n % i != 0 and i <= n // 2:
        i += 1
    return i > n // 2

def TestBinaire(ch):
    n = int(ch)
    chb = ""
    i = 0
    while n != 0:
        chb = str(n % 2) + chb
        n = n // 2
    for c in chb:
        if c == "0":
            i += 1
    return i > 8

def TestDivisibilite(code):
    return int(code[8:]) % int(code[:3]) == 0

def TestFichier(nf, code):
    f = open(nf, "r")
    lg = f.readline()
    tr = False
    while lg != "" and not tr:
        if (lg[:len(lg)-1]) == code:
            tr = True
        else:
            lg = f.readline()
    f.close()
    return tr

def Verif(code):
    if not Premier(code[:3]) or not TestBinaire(code[3:8]) or not TestDivisibilite(code):
        print("Donner un code de recharge valide!")
    else:
        if not TestFichier("Codes.txt", code):
            print("Code déja utilisé!")
        else:
            print("Code valide!")

code = Saisie()
Verif(code)


