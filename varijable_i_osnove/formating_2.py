naslov = "Put u Njemacku"
redatelj = "Hrvatski rukometni savez"
glumac_1 = "Domagoj Duvnjak"
glumac_2 = "Dominik Kuzmanovic"

obrazac = f"Naslov: {naslov}\n\tRedatelj: {redatelj}\n\tGlumci:\n\t\t{glumac_1}\n\t\t{glumac_2}"

obrazac_1 = (f"Naslov: {naslov}\n"
             f"\tRedatelj: {redatelj}\n"
             f"\tGlumci:\n"
             f"\t\t{glumac_1}\n"
             f"\t\t{glumac_2}\n")

obrazac_2 = "Naslov: {}\n\tRedatelj: {}\n\tGlumci:\n\t\t{}\n\t\t{}".format(naslov, redatelj, glumac_1, glumac_2)

print(obrazac)
print(end="\n\n")
print(obrazac_1)
print(end="\n\n")
print(obrazac_2)
