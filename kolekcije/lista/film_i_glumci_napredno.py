naslov = "Put u Njemacku"
redatelj = "Hrvatski rukometni savez"

broj_glumaca=int(input("Dragi korisnice koliko zelis glumaca upisati: "))

glumci = [] #lista()

for indeks in range(broj_glumaca):
    naziv_glumca = input(f"Dragi korisnice unesi ime i prezime {indeks + 1}. glumca: ")
    glumci.append(naziv_glumca)


print(f"Koliko glumaca imamo {len(glumci)}")

osnovno_o_filmu = (f"Naslov: {naslov}\n"
          f"\tRedatelj: {redatelj}\n"
          f"\tGlumci:")

print(osnovno_o_filmu)

for glumac in glumci:
    print(f"\t\t{glumac}")

