naslov = "Put u Njemacku"
redatelj = "Hrvatski rukometni savez"
glumci = ["Domagoj Duvnjak", "Dominik Kuzmanovic",]

glumac_1 = "Domagoj Duvnjak"
glumac_2 = "Dominik Kuzmanovic"

glumci = [glumac_1, glumac_2]

print(f"Koliko glumaca imamo {len(glumci)}")

osnovno_o_filmu = (f"Naslov: {naslov}\n"
          f"\tRedatelj: {redatelj}\n"
          f"\tGlumci:")

print(osnovno_o_filmu)

for glumac in glumci:
    print(f"\t\t{glumac}")

