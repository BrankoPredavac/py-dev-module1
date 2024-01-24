potrosnja_automobila_na_100_km_u_l = float(
    input("Dragi korisnice, koliko litara trosi tvoj auto na 100 km>\n")
)
cijena_goriva_eur_za_1_l = float(
    input(
        "Dragi korisnice, kolika je trenuta cijena goriva u EUR za 1 L kojeg trosi tvoj auto>\n"
    )
)

potrosnja_automobila_na_1_km_u_l = potrosnja_automobila_na_100_km_u_l / 100

cijena_1_km_voznje_u_eur = potrosnja_automobila_na_1_km_u_l * cijena_goriva_eur_za_1_l
cijena_1_km_voznje_u_eur = round(cijena_1_km_voznje_u_eur, 2)

print(end="\n\n")
print("Cijena jednog km voznje iznosi", cijena_1_km_voznje_u_eur, "eur")

dnevna_voznja_do_posla_km = float(input("Dragi korisnice, koliko km imas do posla>\n"))
dnevna_voznja_do_posla_i_nazad_km = 2 * dnevna_voznja_do_posla_km

broj_dana_u_mjesecu = int(
    input("Dragi korisnice, koliko radnih dana ima trenutni mjesec>\n")
)

Ukupna_mjesecna_kilometraza_za_posao = (
    broj_dana_u_mjesecu * dnevna_voznja_do_posla_i_nazad_km
)

mjesecna_cijena_voznje_do_posal_i_nazad_u_eur = round(
    Ukupna_mjesecna_kilometraza_za_posao * cijena_1_km_voznje_u_eur, 2
)

print(end="\n\n")
print(
    "Mjesecna cijena voznje do posla i nazad je",
    mjesecna_cijena_voznje_do_posal_i_nazad_u_eur,
    "eur",
    end="\n\n\n",
)
