broj_zadataka = int(input("Dragi korisnice, koliko planiras danas zadataka obaviti> "))

zadatci = [] # list()

for indeks in range(broj_zadataka):
    novi_zadatak = input(f"Dragi korisnice unesi {indeks + 1}. zadatak kojeg trebas obaviti> ")
    zadatci.append(novi_zadatak)

obavljeni_zadatci = [" "] * broj_zadataka


zagalavlje_redni_broj = "-" * 12
zagalavlje_ime_zdatka = "-" * 60
zagalavlje_obavljen = "-" * 15

zaglavlje = ("+" + zagalavlje_redni_broj + "+" + zagalavlje_ime_zdatka + "+" + zagalavlje_obavljen + "+")

for _ in range(broj_zadataka):
    #Ispis na konzolu
    print("\n\n")
    print(zaglavlje)
    print(f'|{"Redni broj":^12}|{"Naziv zadatka":^60}|{"Obavljen":^15}|')
    print(zaglavlje)
    for indeks_zadatka in range(broj_zadataka):
        redni_broj_str = str(indeks_zadatka + 1) + "."
        print(
            f'|{redni_broj_str:^12}|{zadatci[indeks_zadatka]:^60}|{obavljeni_zadatci[indeks_zadatka]:^15}|'
        )
        print(zaglavlje)

    redni_broj_obavljenog_zadtka = int(input("Unesi redni broj zadtka kojeg si obavio> "))
    indeks_obavljenog_zadtka = redni_broj_obavljenog_zadtka - 1
    obavljeni_zadatci[indeks_obavljenog_zadtka] = "X"

print("\n\n")
print(zaglavlje)
print(f'|{"Redni broj":^12}|{"Naziv zadatka":^60}|{"Obavljen":^15}|')
print(zaglavlje)
for indeks_zadatka in range(broj_zadataka):
    redni_broj_str = str(indeks_zadatka + 1) + "."
    print(
            f'|{redni_broj_str:^12}|{zadatci[indeks_zadatka]:^60}|{obavljeni_zadatci[indeks_zadatka]:^15}|'
        )
    print(zaglavlje)        