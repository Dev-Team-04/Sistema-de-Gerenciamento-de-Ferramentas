from random import randint

lista_part_number = []
for i in range(0,10):
        part_number = randint(10**9, 9*10**9)
        lista_part_number.append(part_number)
print(lista_part_number)
