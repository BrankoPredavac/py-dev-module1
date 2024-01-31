broj_zadataka = int(input("Dragi korisnice, koliko planiras danas zadataka obaviti> "))

zadatci = [] # list()
prioritet_zadatka = []

for indeks in range(broj_zadataka):
    novi_zadatak = input(f"\nDragi korisnice unesi {indeks + 1}. zadatak kojeg trebas obaviti> ")
    zadatci.append(novi_zadatak)
    prioitet_zadtaka = int(input(f"\nDragi korisnice, unesi prioritet zadtka \n{novi_zadatak}\n(nizi prioritet znaci da je zadatak hitniji)\n>"))
    prioritet_zadatka.append(prioitet_zadtaka)    

obavljeni_zadatci = [" "] * broj_zadataka

prioritetni_sortirani = sorted(prioritet_zadatka)
#prioritetni_sortirani = prioritet_zadatka.copy # prioritet_zadatka[:]
#prioritetni_sortirani.sort()

zadatci_sortirani_po_prioritetu = []

for prioritet in prioritetni_sortirani:
    index_proriteta = prioritet_zadatka.index(prioritet)
    prioritet_zadatka.pop(index_proriteta)
    zadatak = zadatci.pop(index_proriteta)
    zadatci_sortirani_po_prioritetu.append(zadatak)

sirina_stupca_redni_broj = 12
sirina_stupca_ime_zadatka = 60
sirina_stupca_prioritet = 10
sirina_stupca_obavljen = 10

zagalavlje_redni_broj = "-" * sirina_stupca_redni_broj
zagalavlje_ime_zdatka = "-" * sirina_stupca_ime_zadatka
zagalavlje_prioritet = "-" * sirina_stupca_prioritet
zagalavlje_obavljen = "-" * sirina_stupca_obavljen

zaglavlje = ("+" + zagalavlje_redni_broj + "+" + zagalavlje_ime_zdatka +"+" + zagalavlje_prioritet +"+" + zagalavlje_obavljen + "+")

redosljed_obavljanja_zadtaka = []

for _ in range(broj_zadataka):
    #Ispis na konzolu
    print("\n\n")
    print(zaglavlje)
    print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Prioritet":^{sirina_stupca_prioritet}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
    print(zaglavlje)
    for indeks_zadatka in range(broj_zadataka):
        redni_broj_str = str(indeks_zadatka + 1) + "."
        print(
            f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci_sortirani_po_prioritetu[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{prioritetni_sortirani[indeks_zadatka]:^{sirina_stupca_prioritet}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
        )
        print(zaglavlje)

    redni_broj_obavljenog_zadtka = int(input("Unesi redni broj zadtka kojeg si obavio> "))
    indeks_obavljenog_zadtka = redni_broj_obavljenog_zadtka - 1
    obavljeni_zadatci[indeks_obavljenog_zadtka] = "X"
    redosljed_obavljanja_zadtaka.append(indeks_obavljenog_zadtka)

print("\n\n")
print(zaglavlje)
print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Prioritet":^{sirina_stupca_prioritet}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
print(zaglavlje)
for indeks_zadatka in range(broj_zadataka):
    redni_broj_str = str(indeks_zadatka + 1) + "."
    print(
        f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci_sortirani_po_prioritetu[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{prioritetni_sortirani[indeks_zadatka]:^{sirina_stupca_prioritet}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
    )
    print(zaglavlje)      


print("\n\n")
print("Dragi korisnice, ovim redosljedom si obavaljao zadatke:")
print("\n\n")
print(zaglavlje)
print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Prioritet":^{sirina_stupca_prioritet}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
print(zaglavlje)
redni_broj = 1
for indeks_zadatka in redosljed_obavljanja_zadtaka:
    redni_broj_str = str(redni_broj) + "."
    print(
            f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci_sortirani_po_prioritetu[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{prioritetni_sortirani[indeks_zadatka]:^{sirina_stupca_prioritet}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
        )
    print(zaglavlje)

    redni_broj += 1   