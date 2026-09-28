def recepte(receptes_numurs):
    if receptes_numurs == "1":
        izmaksas = cukura_cena*aboli_kg*0.3
    else:
        izmaksas = cukura_cena*aboli_kg*0.5
    return izmaksas
receptes_numurs = int(input("Ievadiet receptes numuru:\n1) 1 kg ābolu = 300 gr. cukura\n2) 1 kg ābolu = 500 gr. cukura\n"))
cukura_cena = float(input("Ievadi cukura cenu: "))
abolus_kg = float(input("Ievadi, cik ābolu tev ir (kg): "))

recepte(receptes numurs)

if receptes_numurs == 1:
    cukurs_uz_kg = 0.3 
else:
    cukurs_uz_kg = 0.5 

kopeja_cena = abolus_kg * cukurs_uz_kg * cukura_cena
print(f"Par cukuru tu samaksāsi {kopeja_cena} eiro")
