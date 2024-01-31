broj_zadataka = int(input("Dragi korisnice, koliko planiras danas zadataka obaviti> "))

zadatci = [] # list()

for indeks in range(broj_zadataka):
    novi_zadatak = input(f"Dragi korisnice unesi {indeks + 1}. zadatak kojeg trebas obaviti> ")
    zadatci.append(novi_zadatak)

obavljeni_zadatci = [" "] * broj_zadataka

sirina_stupca_redni_broj = 12
sirina_stupca_ime_zadatka = 60
sirina_stupca_obavljen = 15

zagalavlje_redni_broj = "-" * sirina_stupca_redni_broj
zagalavlje_ime_zdatka = "-" * sirina_stupca_ime_zadatka
zagalavlje_obavljen = "-" * sirina_stupca_obavljen

zaglavlje = ("+" + zagalavlje_redni_broj + "+" + zagalavlje_ime_zdatka + "+" + zagalavlje_obavljen + "+")

redosljed_obavljanja_zadtaka = []

for _ in range(broj_zadataka):
    #Ispis na konzolu
    print("\n\n")
    print(zaglavlje)
    print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
    print(zaglavlje)
    for indeks_zadatka in range(broj_zadataka):
        redni_broj_str = str(indeks_zadatka + 1) + "."
        print(
            f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
        )
        print(zaglavlje)

    redni_broj_obavljenog_zadtka = int(input("Unesi redni broj zadtka kojeg si obavio> "))
    indeks_obavljenog_zadtka = redni_broj_obavljenog_zadtka - 1
    obavljeni_zadatci[indeks_obavljenog_zadtka] = "X"
    redosljed_obavljanja_zadtaka.append(indeks_obavljenog_zadtka)

print("\n\n")
print(zaglavlje)
print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
print(zaglavlje)
for indeks_zadatka in range(broj_zadataka):
    redni_broj_str = str(indeks_zadatka + 1) + "."
    print(
            f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
        )
    print(zaglavlje)        


print("\n\n")
print("Dragi korisnice, ovim redosljedom si obavaljao zadatke:")
print("\n\n")
print(zaglavlje)
print(f'|{"Redni broj":^{sirina_stupca_redni_broj}}|{"Naziv zadatka":^{sirina_stupca_ime_zadatka}}|{"Obavljen":^{sirina_stupca_obavljen}}|')
print(zaglavlje)
redni_broj = 1
for indeks_zadatka in redosljed_obavljanja_zadtaka:
    redni_broj_str = str(redni_broj) + "."
    print(
            f'|{redni_broj_str:^{sirina_stupca_redni_broj}}|{zadatci[indeks_zadatka]:^{sirina_stupca_ime_zadatka}}|{obavljeni_zadatci[indeks_zadatka]:^{sirina_stupca_obavljen}}|'
        )
    print(zaglavlje)

    redni_broj += 1   