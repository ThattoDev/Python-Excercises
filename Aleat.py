#Primeira forma: Este não repete os sorteados
# from random import randint


# result = []
# while len(result) != 2:
#     r = randint(1, 10)
#     if r not in result:
#         result.append(r)
        
# print(result)


#Segunda Forma: Este não repete os números sorteados.
# import random
# result = random.sample(range(0,9), 6)

# print(result)

#Terceira forma
from random import randint

AP_X = [randint(0, 10), randint(0, 100), randint(0, 100), randint(0, 100)]
print(AP_X)