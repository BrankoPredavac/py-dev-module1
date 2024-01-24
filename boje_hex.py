crvena_hex = input("Dragi korisnice daj mi crvenu komponentyu u hex zapisu> ")
crvena_hex_2 = "0x" + crvena_hex

crvena_dek = int(crvena_hex, 16)
crvena_dek_2 = int(crvena_hex_2, 16)

print(crvena_dek)