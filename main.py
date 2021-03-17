import sys
import random

# I. KROK
# Hlavni funkce + vymyslet postup
def hlavni():
    hrac = pridej_hrace()
    hadane_slovo = vyber_hadane_slovo()
    postup, zbyvajici_tahy = schovej_slovo(hadane_slovo)
    while zbyvajici_tahy:
        vypis_stav_hry(hrac, postup, zbyvajici_tahy)
        zbyvajici_tahy = hraci_kolo(hadane_slovo, postup, zbyvajici_tahy)
        konecna_kontrola = posouzeni_stavu(postup, hrac, zbyvajici_tahy, hadane_slovo)
        if konecna_kontrola is not None:  #overuji moznost.
          break
# II. KROK
# Pridame hrace
def pridej_hrace():
    return input("ZADEJTE JMENO: ")
# III. KROK
# Zvolime slovo pro hadani + nacteme jej
def vyber_hadane_slovo():
    with open("slova.txt", "r") as txt:
        obsazena_slova = txt.read().split("\n")
    return random.choice(obsazena_slova)
# IV. KROK
# Schovame jej!
def schovej_slovo(slovo):
    return ["_"] * len(slovo), round(1.3 * len(slovo), 0)
# V. KROK
# Vypisujeme stav hry
def vypis_stav_hry(hr, post, zbyvajici_tahy):
    zprava = f"HRAC: {hr} | STAV: {' '.join(post)} | ZBYVA: {zbyvajici_tahy} |"
    oddelovac = len(zprava) * "-"
    print(oddelovac, zprava, oddelovac, sep="\n")
# VI. KROK
# Hrac hada pismeno
def hrac_hada():
    return input("HADEJ PISMENO: ")
# VII. KROK
# Posouzeni hadaneho pismena
def posouzeni_hadani(pism, slovo, prog):
    for index, letter in enumerate(slovo):
        if letter in pism:
            prog[index] = pism
            print(prog[index])
# VIII. KROK
# Prubeh kazdeho kola
def hraci_kolo(hadane_slovo, postup, zbyvajici_tahy):
    hadane_pismeno = hrac_hada()
    posouzeni_hadani(hadane_pismeno, hadane_slovo, postup)
    zbyvajici_tahy -= 1
    return zbyvajici_tahy
# IX. KROK
# Zaverecny vystup
def posouzeni_stavu(postup, hrac, zbyvajici_tahy, slovo):
    if "_" not in postup:
        vypis_stav_hry(hrac, postup, zbyvajici_tahy)
        print(f"VYBORNE, {hrac}! UHADL JSI!")
        return False #udelal jsem zmenu a funguje to lepe
        # exit()
    elif "_" in postup and zbyvajici_tahy == 0:
        print(f"PROHRALS, {hrac}, BOHUZEL!")
        print(f'Hadane slovo bylo: {slovo}.')
        exit()
hlavni()
