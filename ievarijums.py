cukura_cena = float(input("Ievadi cukura cenu: "))
aboli_kg=float(input("Ievadi, cika abolu tev ir (kg): "))
print(f"Par cukuru tev vajag samaksi {cukura_cena*aboli_kg*0.7} eiro")

receptes_numurs = int(input("Ievadiet receptes numuru:\n1) 1 kg ābolu = 300 gr. cukura\n2) 1 kg ābolu = 500 gr. cukura\n"))

cukura_cena = float(input("Ievadi cukura cenu: "))
abolus_kg = float(input("Ievadi, cik ābolu tev ir (kg): "))
if receptes_numurs == 1:
    cukurs_uz_kg = 0.3 
else:
    cukurs_uz_kg = 0.5 

kopeja_cena = abolus_kg * cukurs_uz_kg * cukura_cena
print(f"Par cukuru tu samaksāsi {kopeja_cena} eiro")
