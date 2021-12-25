from itertools import product
K, M = list( map(int, input().split()) )

matrix =[]
for _ in range(K):
    listi = list( map(int, input().split()) )[1:]
    matrix.append(listi)

productof = list( product(*matrix))
print(productof)
moduluslist  = []
for i in productof:
    j = 0
    for k in i:
        j = j + k**2
    moduluslist.append(j%M)

print(max(moduluslist))


