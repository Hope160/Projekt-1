"""
projekt02.py: druhý projekt do Engeto Online Python Akademie

author: Hana Syblíková
email: syblikovaha@seznam.cz
"""

# Funkce pro vytvoření prázdné hrací desky (3x3)
def inicializuj_desku():
    return [[" "]*3 for _ in range(3)]

# Funkce pro zobrazení aktuálního stavu hrací desky
def vypiš_desku(deska):
    čára = "\t+---+---+---+"
    for i, řádek in enumerate(deska):
        print(čára)
        print("\t| " + " | ".join(řádek) + " |")
    print(čára)

# Funkce kontroluje, zda daný hráč (symbol) vyhrál
def zkontroluj_vítěze(deska, symbol):
    for i in range(3):
        if deska[i].count(symbol) == 3 or all(řádek[i] == symbol for řádek in deska):
            return True
        
    # Kontrola diagonál
    if all(deska[i][i] == symbol for i in range(3)) or all(deska[i][2-i] == symbol for i in range(3)):
        return True
    return False

# Funkce zjišťuje, zda je deska plná (remíza)
def je_plná(deska):
    return all(pole != " " for řádek in deska for pole in řádek)

# Funkce se ptá hráče na jeho tah a ověřuje vstup
def zeptej_se_na_tah(jméno_hráče, deska):
    # Mapa vstupu z čísel 1–9 na pozice v matici (řádek, sloupec)
    pozice = {
        str(i): divmod(i-1, 3) for i in range(1, 10)
    }

    while True:
        tah = input(f"{jméno_hráče}, zadej číslo políčka (1-9): ").strip()
        if tah not in pozice:
            print("Zadej číslo od 1 do 9.")
            continue
        řádek, sloupec = pozice[tah]
        if deska[řádek][sloupec] != " ":
            print("Toto políčko je již obsazené!")
            continue
        return řádek, sloupec

# Hlavní funkce hry, obsahuje herní smyčku
def hraj_piškvorky():
    print("***** PIŠKVORKY OD HANKY *****")
    print("===================================================================")
    print("Pravidla: Vyhrává ten, kdo jako první získá tři své symboly v řadě!")

    # Načtení jmen hráčů
    jméno_O = input("Zadej jméno hráče O: ")
    jméno_X = input("Zadej jméno hráče X: ")
    print("===================================================================")
    # Inicializace skóre hráčů
    skóre = {jméno_O: 0, jméno_X: 0}

    # Herní smyčka pro více kol
    while True:
        deska = inicializuj_desku()
        aktuální_hráč = jméno_O
        aktuální_symbol = "O"

        # Smyčka jednoho kola
        while True:
            vypiš_desku(deska)
            řádek, sloupec = zeptej_se_na_tah(aktuální_hráč, deska)
            deska[řádek][sloupec] = aktuální_symbol

            # Kontrola výhry
            if zkontroluj_vítěze(deska, aktuální_symbol):
                vypiš_desku(deska)
                print(f"🎉 {aktuální_hráč} vyhrává toto kolo!")
                skóre[aktuální_hráč] += 1
                break

            # Kontrola remízy
            if je_plná(deska):
                vypiš_desku(deska)
                print("Remíza!")
                break

            # Střídání hráčů
            if aktuální_hráč == jméno_X:
                aktuální_hráč, aktuální_symbol = jméno_O, "O"
            else:
                aktuální_hráč, aktuální_symbol = jméno_X, "X"

        # Výpis skóre po kole
        print(f"Skóre: {jméno_O} {skóre[jméno_O]} - {jméno_X} {skóre[jméno_X]}")

        # Dotaz na další hru
        znovu = input("Chceš hrát znovu? (ano/ne): ").strip().lower()
        if znovu != "ano":
            print("===================================================================")
            break
        
# Spuštění programu
if __name__ == "__main__":
    hraj_piškvorky()