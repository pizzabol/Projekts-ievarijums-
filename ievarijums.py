cukura_cena = float(input("Ievadi cukura cenu: "))
aboli_kg=float(input("Ievadi, cika abolu tev ir (kg): "))
print(f"Par cukuru tev vajag samaksi {cukura_cena*aboli_kg*0.7} eiro")

receptes_numurs = int(input("Ievadiet receptes numuru:\n1) 1 kg ābolu = 300 gr. cukura\n2) 1 kg ābolu = 500 gr. cukura\n"))
cukura_cena = float(input("Ievadi cukura cenu: "))
abolus_kg = float(input("Ievadi, cik ābolu tev ir (kg): "))
if receptes_numurs == 1:
    cukurs_uz_kg = 0.3 
else:
    izmaksas = cukura_cena*abolus_kg*0.5 
print(f"Par cukuru tu samaksāsi {izmaksas} eiro")
print(":) otrais zars")