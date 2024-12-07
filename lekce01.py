# indexování
# Vypiš 5 prvníh znaků
print("Prvních 5 písmen:")
print("indexování"[:5])

# Vypiš posledních 5 znaků
print("Posledních 5 písmen:")
print("indexování"[-5:])

# Vypiš každý 3 znak
print("Každé 3. písmeno (počínaje prvním) od 'i':")
print("indexování"[::3])

# převody jednotek
kg_lb = 2.20
km_mile = 0.62
l_gal = 0.26

kg_pocet = 80
km_pocet = 54
l_pocet = 5

print(kg_pocet,'kg je', kg_pocet * kg_lb, 'lb')
print(km_pocet, 'km je', km_pocet * km_mile, 'mile')
print(l_pocet, 'l je', l_pocet * l_gal, 'gal')

#ceník
mercedes = 150_000
rolls_royce = 400_000
vybava = 50_000
sleva = 5_000

#Sleva na Mercedes: 5000
#Cena za dva Mercedesy je: 300000
#Cena za Mercedes a Rolls-Royce: 550000
#Cena za dva Rolls-Royce s příplatkovou výbavou: 900000
#Cena za Mercedes s příplatkovou výbavou: 200000
#Cena za Mercedes po slevě: 145000

Sleva_na_Mercedes_je = sleva
Cena_za_dva_Mercedesy_je = 2 * mercedes
Cena_za_Mercedes_a_RollsRoyce = mercedes + rolls_royce
Cena_za_dva_RollsRoyce_s_příplatkovou_výbavou = 2 * rolls_royce + 2 * vybava
Cena_za_Mercedes_s_příplatkovou_výbavou = mercedes + vybava
Cena_za_Mercedes_po_slevě = mercedes - sleva

print('Sleva na mercese je', Sleva_na_Mercedes_je)
print ('Cena za dva Mercedesy je', Cena_za_dva_Mercedesy_je)
print('Cena za Mercedes a Rolls-Royce je:', Cena_za_Mercedes_a_RollsRoyce)
print('Cena za dva Rolls-Royce je:', Cena_za_dva_RollsRoyce_s_příplatkovou_výbavou)
print('Cena za Mercedes s příplatkovou výbvou je:', Cena_za_Mercedes_s_příplatkovou_výbavou)
print('Cena za Mercedes po slevě je:',Cena_za_Mercedes_po_slevě)

jmeno = 'Lukáš'
prijmeni = ' Dvořák'
cele_jmeno = jmeno + prijmeni
delka_jmena = len(cele_jmeno)
cele_jmeno_1 = ('='* delka_jmena)


print('Celé jméno', cele_jmeno)
print('Délka jména', delka_jmena)
print(cele_jmeno_1)
print(cele_jmeno)
print(cele_jmeno_1)


