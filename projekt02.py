"""
projekt02.py: druhý projekt do Engeto Online Python Akademie

author: Hana Syblíková
email: syblikovaha@seznam.cz
"""
def inicializuj_desku():
    return [[" "]*3 for _ in range(3)]

def vypiš_desku(deska):
    čára = "\t+---+---+---+"
    for i, řádek in enumerate(deska):
        print(čára)
        print("\t| " + " | ".join(řádek) + " |")
    print(čára)

def zkontroluj_vítěze(deska, symbol):
    for i in range(3):
        if deska[i].count(symbol) == 3 or all(řádek[i] == symbol for řádek in deska):
            return True
    if all(deska[i][i] == symbol for i in range(3)) or all(deska[i][2-i] == symbol for i in range(3)):
        return True
    return False

def je_plná(deska):
    return all(pole != " " for řádek in deska for pole in řádek)

def zeptej_se_na_tah(jméno_hráče, deska):
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

def hraj_piškvorky():
    print("=== PIŠKVORKY ===")
    print("Pravidla: Vyhrává ten, kdo jako první získá tři své symboly v řadě!")

    jméno_O = input("Zadej jméno hráče O: ")
    jméno_X = input("Zadej jméno hráče X: ")
    skóre = {jméno_O: 0, jméno_X: 0}

    while True:
        deska = inicializuj_desku()
        aktuální_hráč = jméno_O
        aktuální_symbol = "O"

        while True:
            vypiš_desku(deska)
            řádek, sloupec = zeptej_se_na_tah(aktuální_hráč, deska)
            deska[řádek][sloupec] = aktuální_symbol

            if zkontroluj_vítěze(deska, aktuální_symbol):
                vypiš_desku(deska)
                print(f"🎉 {aktuální_hráč} vyhrává toto kolo!")
                skóre[aktuální_hráč] += 1
                break

            if je_plná(deska):
                vypiš_desku(deska)
                print("Remíza!")
                break

            # změna hráče
            if aktuální_hráč == jméno_X:
                aktuální_hráč, aktuální_symbol = jméno_O, "O"
            else:
                aktuální_hráč, aktuální_symbol = jméno_X, "X"

        print(f"Skóre: {jméno_X} {skóre[jméno_X]} - {jméno_O} {skóre[jméno_O]}")
        znovu = input("Chceš hrát znovu? (ano/ne): ").strip().lower()
        if znovu != "ano":
            break

if __name__ == "__main__":
    hraj_piškvorky()