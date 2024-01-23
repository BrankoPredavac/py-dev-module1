jedan_mjesec_u_danima = int(input("Dragi korisnice koliko dana ima ovaj mjesec> "))
snaga_mikrovalne_pecnice_u_kw = float(input("Dragi korisnice koliko je jaka tvoja mikrovlana pecnica u kW> "))
koristenje_mikrovalne_h_po_1_dan = int(input("Dragi korisnice koliko sati dnevno radi vasa mikrovlana> "))
cijena_struje_eur_po_1_kwh = float(input("Dragi korisnice koliko je cijena struje za 1 kWh> "))

dnevna_potrosnja_mikrovlana_kwh = snaga_mikrovalne_pecnice_u_kw * koristenje_mikrovalne_h_po_1_dan

mjesecna_potrosnja_mikrovlana_kwh = jedan_mjesec_u_danima * dnevna_potrosnja_mikrovlana_kwh

mjesecna_cijena_mikrovlana_struja_eur = mjesecna_potrosnja_mikrovlana_kwh * cijena_struje_eur_po_1_kwh

print(end = "\n\n\n")

print("Racun za jedan mjesec mikorvalne pecnice snage",
      snaga_mikrovalne_pecnice_u_kw,
      "kW",
      "koja se koristi",
      koristenje_mikrovalne_h_po_1_dan,
      "h dnevno,"
      "iznosi",
      mjesecna_cijena_mikrovlana_struja_eur,
      "eur", end="\n\n\n")

