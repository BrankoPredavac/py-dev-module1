recenica = input("Dragi korisnice, daj mi jednu rijec za koju zelsi provjeriti je li palindrom> ")

lista_rijeci = recenica.lower().strip().split()
rijec = "".join(lista_rijeci)

# p1 = input("Dragi korisnice, daj mi jednu rijec za koju zelsi provjeriti je li palindrom> ")
# p2 = p1.lower()
# p3 = p2.strip()
# lista_rijeci = p3.split()


list_znakova = list(rijec)

obrnuta_lista = list(reversed(list_znakova))

je_li_palindrom = list_znakova == obrnuta_lista

print(f"{recenica} je palindorm: {je_li_palindrom}")