# Vyzkoušej si spustit tento zápis!
jmeno = "Marek"

if jmeno == "Marek":
 print("Ahoj, Marku!")

 # Vyzkoušej si spustit tento zápis!
jmeno = "Lukas"

if jmeno == "Marek":
 print("Ahoj, Marku!")

muj_seznam_1 =  [
    'František', 'Bruno',
    'Anna', 'Jakub',
    'Klára', 'Anežka',
    'Anežka', 'Anežka'
]
#Na indexu 2 je: Anna
#Na 7 indexu je: Anežka
#V intervalu od 2 do 5 je: ['Anna', 'Jakub', 'Klára', 'Anežka']
#Každý třetí člen je: ['František', 'Jakub', 'Anežka']

print('Na indexu 2 je: ',muj_seznam_1[2])
print('Na posledním indexu je:',muj_seznam_1[7])
print('V intervalu od 2 do 5 je:',muj_seznam_1[2:6])
print('Každý třetí člen je:',muj_seznam_1[::3])

jmeno_01 = 'Martin'
vaha = 80
vyska  = 2
BMI = vaha / vyska ** 2

if BMI > 40:
    kategorie = 'těžká obezita'
elif BMI > 30:
    kategorie = 'obezita'
elif BMI > 25:
    kategorie = 'mírná nadváha'
elif BMI > 18.5:
    kategorie = 'zdravá váha'
else:
    kategorie = 'podvýživa'

print(jmeno_01,"tvé BMI je", BMI,",což spadá do kategorie",kategorie, ".")

zamestnanci = [
   'František','Anna',
   'Jakub','Klára'
   ]
print('Zaměstnanci na začátku:',zamestnanci)
zamestnanci_a = zamestnanci.copy()
zamestnanci_a.append('Bruno')
zamestnanci_a.append('Anežka')
print('Nová jména přidána: ', zamestnanci_a)
zamestnanci_b = zamestnanci.copy()
zamestnanci_b.insert(1, 'Bruno')
print('Nová jména vložená:',zamestnanci_b)

vstupni_cisla = [1, 2, 3, 4, 5, 6, 7]
vstupni_pismena = ["p", "ú", "s", "č", "p", "s", "n"]
tyden = ('pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle')

cislo_dne = 5
if cislo_dne in vstupni_cisla:
    print("Správná vstupní hodnota!")
    den_tydne = tyden[cislo_dne - 1]
    if den_tydne.startswith(vstupni_pismena[cislo_dne - 1]):
        print("Správné písmeno")
    else:
        print("Špatné písmeno!")

else:
    print("Špatná vstupní hodnota!")


