"""
projekt01.py: první projekt do Engeto Online Python Akademie

author: Hana Syblíková
email: syblikovaha@seznam.cz
"""
# začátek kódu
print(40 * "*")
print(
"""Vítej v textovém analyzátoru od Hanky :-)
========================================
Níže zadej své uživatelské jméno a heslo"""
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

print("\nUkázky textů, které můžete analyzovat:", "\n" "\n1. ",Text_1, "\n2. ",Text_2,"\n3. ",Text_3 )
print(40 * "=")

#volba textu uživatelem
try:
        volba = int(input("Zadejte číslo pro vybrání textu (1-3): "))
        if volba < 1 or volba > 3:
            print("Neplatná volba. Program bude ukončen.")
            exit()
        print(40 * "=")
        print(f"\nVybrali jste text číslo: {volba}")
except ValueError:
        print("Neplatný vstup. Zadejte prosím číslo mezi 1 a 3.")
        exit()  # Ukončí program

print(40 * "=")
#vypsání vybraného textu se kterým se bude dál pracovat
if volba == 1:
    print("\nText Vašeho výběru zní:\n", Text_1)
if volba == 2:
    print("\nText Vašeho výběru zní:\n", Text_2)
if volba == 3:
    print("\nText Vašeho výběru zní:\n", Text_3)
print(40 * "=")
            
#Samotná analýza vybraného textu
text = TEXTS[volba - 1]
import string  
# seznam hodnot z úkolu
pocet_slov = len(text.split())
slova_s_velkym_pismenem = sum(1 for word in text.split() if word.istitle())
velka_slovna = sum(1 for word in text.split() 
                   if word.isupper() and word.strip(string.punctuation).isalpha())
mala_slovna = sum(1 for word in text.split() if word.islower())
ciselne_retezce = sum(1 for word in text.split() if word.isdigit())
soucet_cisel = sum(int(word) for word in text.split() if word.isdigit())

print("\nAnalýza Vášeho textu:") # Výstupy
print(40*'-')
print(f"Ve vybraném textu je {pocet_slov} slov.")
print(40*'-')
print(f"Ve vybraném textu je {slova_s_velkym_pismenem} slov s velkým písmenem.")
print(40*'-')
print(f"Ve vybraném textu je {velka_slovna} slov napsaných velkými písmeny.")
print(40*'-')
print(f"Ve vybraném textu je {mala_slovna} slov napsaných malými písmeny.")
print(40*'-')
print(f"Ve vybraném textu je {ciselne_retezce} číselných řetězců.")
print(40*'-')
print(f"Soucet všech čísel je {soucet_cisel}")
print(27*'*')
print(40 * "=")

print(f" {'LEN':<4}|{'OCCURRENCES ':^19}|{' NR.':>3}")
delka_slov = [len (word.strip(string.punctuation)) for word in text.split()] # seznamu délky každého slova
mnozina_delka = set(delka_slov) # Vytvoření množiny délek slov
frekvence_delka = [] # frekvence jednotlivých délek slov
for delka in mnozina_delka:
    frekvence_delka.append(delka_slov.count(delka))
nejvyssi_delka = max(frekvence_delka)
# tabulka
star = '*'
space = ' '
for delka in mnozina_delka:
    pocet_space = nejvyssi_delka - delka_slov.count(delka)
    print(f" {delka:<4}| {star * delka_slov.count(delka):<18}| {delka_slov.count(delka):>3}")
print(40 * "=")
print("Děkujeme za využití textového analyzátoru od Hanky :-)")
print(40 *'*')