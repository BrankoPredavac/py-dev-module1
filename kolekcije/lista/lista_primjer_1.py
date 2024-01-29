moja_prazna_lista = []
print(type(moja_prazna_lista))

moja_prazna_lista_1 = list()
print(type(moja_prazna_lista_1))

# Cuva poredak elemenata
moja_raznovrna_lista = ["Moje ime", 9.8, 10, True, False, "Moje ime", 11, 10, 11, True]
print(moja_raznovrna_lista)

print("\n\n")
lista_voca =  ["jabuka", "banana", "tresnja"]
print(lista_voca)

# print("\n\n")
# lista_korisnika =  ["Ana", "Marko", "Mate"]
# print(lista_korisnika)
# lista_korisnika.clear()
# print(lista_korisnika)

print("\n\n")
lista_voca.append("kruska")
lista_voca.append("jabuka")
print(lista_voca)

broj_krusaka = lista_voca.count("kruska")
broj_krusaka_2 = lista_voca.count("Kruska")
broj_jabuka = lista_voca.count("jabuka")
broj_lubenica = lista_voca.count("lubenica")

print(f"Broj jabuka: {broj_jabuka}\nBroj krusaka: {broj_krusaka}\nBroj lubenica: {broj_lubenica}")
print("Broj Krusaka:  {broj_krusaka_2}")

novo_voce_iz_trgovine = ["ribizl", "mandarina"]
lista_voca.extend(novo_voce_iz_trgovine)
print("\n\n")
print(lista_voca)

index_kruska = lista_voca.index("kruska")
print(f"Index kruske je {index_kruska}")

# Index funkcija ocekuje da imamo taj element u listi
# index_lubenica = lista_voca.index("lubenica")
# print(f"Index lubenice je {index_lubenica}")

index_jabuka = lista_voca.index("jabuka")
print(f"Index jabuka je {index_jabuka}")

print(f"Voce na indeksu 6 je {lista_voca[6]}")
print(f"Voce na indeksu 3 je {lista_voca[3]}")
print(f"Voce na indeksu 0 je {lista_voca[0]}")

# print(f"Voce na indeksu 99 je {lista_voca[99]}")

print("\n\n")
lista_voca.insert(3, "lubenica")
print(lista_voca)

print("\n\n")
lista_voca.remove("kruska")
print(lista_voca)

print("\n\n")
lista_voca.remove("jabuka")
print(lista_voca)

# print("\n\n")
# lista_voca.remove("dinja")
# print(lista_voca)

print("\n\n")
vraca_nam_vrijednost = lista_voca.pop(4)
print(f"Element koji smo makli s indeksa 4 je {vraca_nam_vrijednost}")
print(lista_voca)

print("\n\n")
vraca_nam_vrijednost = lista_voca.pop()
print(f"Element koji smo makli s indeksa 4 je {vraca_nam_vrijednost}")
print(lista_voca)

print("\n\nPrije reversa")
print(lista_voca)
lista_voca.reverse()
print("Poslije reversa")
print(lista_voca)


print("\n\nPrije sorta")
print(lista_voca)
lista_voca.sort()
print("Poslije sorta")
print(lista_voca)

print("\n\nPrije sorta")
print(lista_voca)
lista_voca.sort(reverse=True)
print("Poslije sorta")
print(lista_voca)

print("Gotovo")