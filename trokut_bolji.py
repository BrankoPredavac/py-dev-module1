import math

stranica_trokuta_a_cm = float(input("Dragi korisnice, molim te reci mi koliko je duga stranica trokuta a, u cm>\n"))
stranica_trokuta_b_cm = float(input("Dragi korisnice, molim te reci mi koliko je duga stranica trokuta b, u cm>\n"))
stranica_trokuta_c_cm = float(input("Dragi korisnice, molim te reci mi koliko je duga stranica trokuta c, u cm>\n"))

opseg_trokuta_cm = stranica_trokuta_a_cm + stranica_trokuta_b_cm + stranica_trokuta_c_cm

visina_na_stranicu_a_cm = stranica_trokuta_a_cm * math.sqrt(3) / 2

povrsina_trokuta_cm2 = round(stranica_trokuta_a_cm * visina_na_stranicu_a_cm / 2, 4)

print("\n")
print("Opseg trokuta iznosi: ", opseg_trokuta_cm, "cm")
print("\n")
print("Površina trokuta iznosi: ", povrsina_trokuta_cm2, "cm^2")
print(f"Površina trokuta iznosi: {povrsina_trokuta_cm2:.2f} cm^2")
print("\n") 
