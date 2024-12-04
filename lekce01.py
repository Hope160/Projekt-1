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