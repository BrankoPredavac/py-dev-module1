broj_imena = int(input("Dragi korisncie, koliko imena zelis unjeti> "))

lista_imena = []

for indeks in range(broj_imena):
    novo_ime = input(f"Dragi korisnice, upisi {indeks + 1}. ime> ")
    lista_imena.append(novo_ime)

print("\n\nDragi korisncie ovo su sva imena:")
for ime in lista_imena:
    print(ime, end=", ")

odabrano_ime = input("\nDragi korisnice, od pondudenih imena odaberi jedno> ")

indeks_imena = lista_imena.index(odabrano_ime)

lista_imena = lista_imena * 4

print(f"Odabrano ime je: {odabrano_ime}")

indeks_za_tri_mjesta_u_desno = (indeks_imena + 3)

print(f"Od tog imena za 3 mjesta u desno se nalazi {lista_imena[indeks_za_tri_mjesta_u_desno]}")

indeks_za_pet_mjesta_u_desno = (indeks_imena + 5)

print(f"Od tog imena za 5 mjesta u desno se nalazi {lista_imena[indeks_za_pet_mjesta_u_desno]}")

