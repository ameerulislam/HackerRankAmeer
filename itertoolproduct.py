from itertools import product

A = input().split()
B = input().split()
product_of = product(A, B)
product_of = list(product_of)

secondlist = []
tuples = []
for i in product_of:
    for l in i:
        tuples.append(int(l))
    secondlist.append(tuple(tuples))
    tuples.clear()
secondlist = tuple(secondlist)
# print(secondlist)
print( ' '.join(map(str, secondlist)))