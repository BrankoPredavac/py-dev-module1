lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

lista_3 = lista_1 + lista_2
print(lista_3)

lista_4 = lista_2 + lista_1
print(lista_4)

lista_a = [1, 2, 3]
lista_a = lista_a * 3
print(lista_a)

voca = ["jabuka", "kruska", "sljiva"]
print("jabuka" in voca)
print("lubenica" not in voca)

print("\n\n")
voca = ["jabuka", "kruska", "sljiva"]
print("jabuka" not in voca)
print("lubenica" in voca)

print(lista_1 == [1, 2, 3])

moj_string = "banana"
moj_string_lista = list(moj_string)
print(moj_string_lista)
print(type(moj_string_lista[0]))