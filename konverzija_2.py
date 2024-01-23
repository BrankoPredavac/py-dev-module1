bin_str = bin(756)

print(type(bin_str))
print(bin_str)

oct_str = oct(756)

print(type(oct_str))
print(oct_str)

hex_str = hex(756)

print(type(hex_str))
print(hex_str)


dekatski_str = int("756")
print(dekatski_str)

bin_to_dek = int(bin_str, base = 2)
print("bin_to_dek", bin_to_dek)

oct_to_dek = int(oct_str, base = 8)
print("oct_to_dek", oct_to_dek)

hex_to_dek = int(hex_str, base = 16)
print("hex_to_dek", hex_to_dek)