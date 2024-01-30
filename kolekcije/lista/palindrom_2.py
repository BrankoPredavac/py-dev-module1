rijec = input("Dragi korisnice, daj mi jednu rijec za koju zelsi provjeriti je li palindrom> ").lower().strip()

list_znakova = list(rijec)

obrnuta_lista = list_znakova.copy()
obrnuta_lista.reverse()

je_li_palindrom = list_znakova == obrnuta_lista

print(f"Rijec {rijec} je palindorm: {je_li_palindrom}")