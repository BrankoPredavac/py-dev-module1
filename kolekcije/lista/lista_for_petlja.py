smocnica = ["jabuka", "visnja", "dinja", "lubenica"]
zeli_li_jesti = []


print("Pocetak")

for jedno_voce in smocnica:
    odgovor_korisnika = input(f"Zelite li jesti {jedno_voce}? ")
    zeli_li_jesti.append(odgovor_korisnika)
    print(jedno_voce)


print("Gotovo")