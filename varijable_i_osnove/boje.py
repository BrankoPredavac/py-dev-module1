crvena = int(input("Dragi korisnice reci koliko je jaka crvena komponenta (0-255)> "))
zelena = int(input("Dragi korisnice reci koliko je jaka zelena komponenta (0-255)> "))
plava = int(input("Dragi korisnice reci koliko je jaka plava komponenta (0-255)> "))

crvena_hex = hex(crvena)
zelena_hex = hex(zelena)
plava_hex = hex(plava)

print()
print("Hex vrijednost vase boje")
print("#", crvena_hex, zelena_hex, plava_hex, sep="")
# print("#", crvena_hex[2:], zelena_hex[2:], plava_hex[2:], sep="")

print(crvena_hex, zelena_hex, plava_hex, sep="-")

crvena_dek = int(crvena_hex, 16)
zelena_dek = int(zelena_hex, 16)
plava_dek = int(plava_hex, 16)

print("(R, G, B)")
print(crvena_dek, zelena_dek, plava_dek, sep=", ")

print("(" + str(crvena_dek) + ", " + str( zelena_dek) + ", " + str(  plava_dek)+ ")")