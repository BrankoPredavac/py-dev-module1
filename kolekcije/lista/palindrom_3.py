rijec = input("Dragi korisnice, daj mi jednu rijec za koju zelsi provjeriti je li palindrom> ").lower().strip()

list_znakova = list(rijec)

obrnuta_lista = list_znakova.copy()
obrnuta_lista.reverse()

je_li_palindrom = True

for indeks in range(len(list_znakova)):
    if je_li_palindrom and list_znakova[indeks] != obrnuta_lista[indeks]:
        je_li_palindrom = False

print(f"Rijec {rijec} je palindorm: {je_li_palindrom}")