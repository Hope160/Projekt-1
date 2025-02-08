"""
projekt01.py: první projekt do Engeto Online Python Akademie

author: Hana Syblíková
email: syblikovaha@seznam.cz
"""
# začátek textového editoru
print(40 * "*")
print(
"""Vítej v textovém editoru od Hanky :-)
========================================
Níže zasej své uživatelské jméno a heslo"""
)
print(40 * "*")


# uživatelé a jejich hesla ze zadání
registrovani_uzivatele = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}

#výzva k zadání jména a hesla + ověření shody
def prihlaseni():
    
    jmeno = input("Zadejte přihlašovací jméno: ")
    heslo = input("Zadejte heslo: ")
    print(40 * "*")
    
    if jmeno in registrovani_uzivatele and registrovani_uzivatele[jmeno] == heslo:
        print(f"Pěkný den, vítám tě, {jmeno}! Můžete začít analyzovat texty.")
        
    else:
        print("Neplatné přihlašovací údaje. Program bude ukončen.")
        exit()  

prihlaseni()

#oddělení přihlášení od výběru textu
print(40 * "=")

TEXTS = ['''
Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''',
'''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''',
'''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.'''
]

Text_1 = ['''Situated about 10 miles west of Kemmerer,
Fossil Butte is a ruggedly impressive
topographic feature that rises sharply
some 1000 feet above Twin Creek Valley
to an elevation of more than 7500 feet
above sea level. The butte is located just
north of US 30N and the Union Pacific Railroad,
which traverse the valley. ''']

Text_2 = ['''At the base of Fossil Butte are the bright
red, purple, yellow and gray beds of the Wasatch
Formation. Eroded portions of these horizontal
beds slope gradually upward from the valley floor
and steepen abruptly. Overlying them and extending
to the top of the butte are the much steeper
buff-to-white beds of the Green River Formation,
which are about 300 feet thick.''']

Text_3 = ['''The monument contains 8198 acres and protects
a portion of the largest deposit of freshwater fish
fossils in the world. The richest fossil fish deposits
are found in multiple limestone layers, which lie some
100 feet below the top of the butte. The fossils
represent several varieties of perch, as well as
other freshwater genera and herring similar to those
in modern oceans. Other fish such as paddlefish,
garpike and stingray are also present.''']

#ukázky textů uživateli ze kterých může vybírat
def vyber_text():
    print("\nVyberte číslo textu, který chcete analyzovat:")
    print(Text_1)
    print(Text_2)
    print(Text_3)

#volba textu uživatelem
try:
        volba = int(input("Zadejte číslo pro vybrání textu (1-3): "))
        if volba < 1 or volba > 3:
            print("Neplatná volba. Program bude ukončen.")
            exit()
        print(40 * "=")
        print(f"\nVybrali jste text číslo: \n{volba}")
except ValueError:
        print("Neplatný vstup. Zadejte prosím číslo mezi 1 a 3.")
        exit()  # Ukončí program

#vypsání vybraného textu se kterým se bude dál pracovat
if volba == 1:
    print("Text Vašeho výběru zní:", Text_1)
if volba == 2:
    print("Text Vašeho výběru zní:", Text_2)
if volba == 3:
    print("Text Vašeho výběru zní:", Text_2)
            
#Samotná analýza vybraného textu
text = TEXTS[volba - 1]

# seznam hodnot z úkolu
pocet_slov = len(text.split())
slova_s_velkym_pismenem = sum(1 for word in text.split() if word.istitle())
velka_slovna = sum(1 for word in text.split() 
                   if word.isupper() and word.strip(string.punctuation).isalpha())
mala_slovna = sum(1 for word in text.split() if word.islower())
ciselne_retezce = sum(1 for word in text.split() if word.isdigit())
soucet_cisel = sum(int(word) for word in text.split() if word.isdigit())

# Výstupy
print(40*'-')
print(f"V vybraném textu je {pocet_slov} slov.")
print(40*'-')
print(f"V vybraném textu je {slova_s_velkym_pismenem} slov s velkým písmenem.")
print(40*'-')
print(f"V vybraném textu je {velka_slovna} slov napsaných velkými písmeny.")
print(40*'-')
print(f"V vybraném textu je {mala_slovna} slov napsaných malými písmeny.")
print(40*'-')
print(f"V vybraném textu je {ciselne_retezce} číselných řetězců.")
print(40*'-')
print(f"Soucet všech čísel je {soucet_cisel}")
print(40*'*')
# poslední část je graf
print(40 * "=")


#zde jsem skončila a je nutno dál kontrolovat a propojovat
print(f" {'LEN':<3}|{'OCCURRENCES':^17}|{'NR.':>4}")
# seznamu délky každého slova
delka_slov = [len(word.strip(string.punctuation)) for word in text.split()]
# Vytvoření množiny délek slov
mnozina_delka = set(delka_slov)
# frekvence jednotlivých délek slov
frekvence_delka = []
for delka in mnozina_delka:
    frekvence_delka.append(delka_slov.count(delka))
nejvyssi_delka = max(frekvence_delka)
# tabulka
star = '*'
space = ' '
for delka in mnozina_delka:
    pocet_space = nejvyssi_delka - delka_slov.count(delka)
    print(f" {delka} | {star * delka_slov.count(delka)} {space * pocet_space} | {delka_slov.count(delka)}")
print(40 * "=")

