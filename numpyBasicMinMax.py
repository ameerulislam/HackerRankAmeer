# import numpy as np
# nxm = list(map(int, input().split()))
# listi = []
# for _ in range(nxm[0]):
#     listi.append( list(map(int,  input().split())) )

# listi = np.array(listi)
# listi_mins = listi.min(axis=1)
# print(max(listi_mins))

import numpy
print(numpy.max(numpy.min(numpy.array([input().split() for _ in range(int(input().split()[0]))],int),axis=1)))