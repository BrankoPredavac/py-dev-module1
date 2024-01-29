lista_voca_i_povrca = ["jabuka", "sljiva", "ananas", "dinja", "rajcica", "luk"]

print(f"Duljina liste voce i povrce je {len(lista_voca_i_povrca)}")

print(f'Broj znakova u recenici "Dobro jutro svima." je {len("Dobro jutro svima.")}')

lista_voca_i_povrca.sort()
print(lista_voca_i_povrca)

lista_voca_i_povrca.sort(key = lambda x: len(x))
print(lista_voca_i_povrca)


lista_voca_i_povrca_2 = ["jabuka", "sljiva", "ananas", "dinja", "rajcica", "luk"]

print("\n\n")
sortirana_po_duljini_naziva = sorted(lista_voca_i_povrca_2, key = lambda x: len(x))
print(lista_voca_i_povrca_2)
print(sortirana_po_duljini_naziva)

print("\n\n")
obrnuta_lista_voce_povrce = list(reversed(lista_voca_i_povrca_2))
print(lista_voca_i_povrca_2)
print(obrnuta_lista_voce_povrce)