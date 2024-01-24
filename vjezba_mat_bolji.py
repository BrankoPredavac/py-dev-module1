prvi_broj = input("Dragi korisnice, molim te unesi prvi broj> ")
prvi_broj = float(prvi_broj)
drugi_broj = float(input("Dragi korisnice, molim te unesi drugi broj (molim te ne unosi 0)> "))

zbroj = prvi_broj + drugi_broj
print(prvi_broj, "+", drugi_broj, "=", zbroj, end="\n\n\n")

razlika = prvi_broj - drugi_broj
print(prvi_broj, "-", drugi_broj, "=", razlika, end="\n\n\n")

umnozak = prvi_broj * drugi_broj
print(prvi_broj, "*", drugi_broj, "=", umnozak, end="\n\n\n")

djeljenja = prvi_broj / drugi_broj
print(prvi_broj, "/", drugi_broj, "=", djeljenja, end="\n\n\n")

potenciranje = prvi_broj ** drugi_broj
print(prvi_broj, "^", drugi_broj, "=", potenciranje, end="\n\n\n")

ostatak_djeljenja = prvi_broj % drugi_broj
print(prvi_broj, "%", drugi_broj, "=", ostatak_djeljenja, end="\n\n\n")

cjelobrojno_djeljenje = prvi_broj // drugi_broj
print(prvi_broj, "//", drugi_broj, "=", cjelobrojno_djeljenje, end="\n\n\n")
