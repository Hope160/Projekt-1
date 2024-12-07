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

