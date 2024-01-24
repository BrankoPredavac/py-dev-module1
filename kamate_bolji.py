iznos_za_stednju_u_eur = float(input("Dragi korisnice koliko novaca mislis orocit u eur>\n"))
vrijeme_stednje_u_godinama = int(input("Dragi korisnice koliko godina mislis stedjeti>\n"))
godisnja_kamata_u_postotku = float(input("Dragi korisnice koliku kamatnu stopu ti banka nudi>\n"))

vrijednost_kamate_u_eur = iznos_za_stednju_u_eur * vrijeme_stednje_u_godinama * (godisnja_kamata_u_postotku / 100)
print("\n")

moj_lijepsi_ispis = "Iznos kamate nakon " + str(vrijeme_stednje_u_godinama) + " godina štednje iznosi uz kamatnu stopu " + str(godisnja_kamata_u_postotku) +  " % iznosi: " + str(vrijednost_kamate_u_eur) + " EUR"

print(moj_lijepsi_ispis)

print("Iznos kamate nakon", vrijeme_stednje_u_godinama ,"godina štednje iznosi uz kamatnu stopu", godisnja_kamata_u_postotku , "% iznosi:", vrijednost_kamate_u_eur, "eur")

print(f"Iznos kamate nakon {vrijeme_stednje_u_godinama:.1f} godina štednje iznosi uz kamatnu stopu {godisnja_kamata_u_postotku:.2f} % iznosi: {vrijednost_kamate_u_eur:.2f} eur")

print("\n") 