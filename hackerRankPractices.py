k = 2
lista = [9, 5, 4, 2, 6, 15, 12]

def hackerlandRadioTransmitters(x, k):
    # Write your code here
    x_min = min(x)
    x_max = max(x)
    # print(x_min, x_max)
    # x_min_pointer = x_min
    # coverageRange = (k*2)+1
    x.sort()
    c = 0
    i=0
    upperLimitforI = min(x)
    while i < len(x):
        print("i's: ", x[i])

        if upperLimitforI < x[i]:
            upperLimitforI = upperLimitforI +(k*2)
        else:
            upperLimitforI = x[i] +(k*2)

        print("upperLimitforI ", upperLimitforI)

        j=0
        while j < len(x):
            if x[j] <= upperLimitforI:
                poppsedvalue = x.pop(x.index(x[j]))
                print("popped value: ", poppsedvalue)
                print(x)
            else:
                j+=1
        
        upperLimitforI = poppsedvalue + 1
        c +=1
        print ("station number", c)
    print("How many stations in total? ", c)

hackerlandRadioTransmitters(lista, k)
















# k = 2
# lista = [9, 5, 4, 2, 6, 15, 12]

# def hackerlandRadioTransmitters(x, k):
#     # Write your code here
#     x_min = min(x)
#     x_max = max(x)
#     # print(x_min, x_max)
#     # x_min_pointer = x_min
#     # coverageRange = (k*2)+1
#     x.sort()
#     c = 0
#     i=0
#     while i < len(x):
#         print("i's: ", x[i])
#         upperLimitforI = x[i] +(k*2)
#         print("upperLimitforI ", upperLimitforI)

#         j=0
#         while j < len(x):
#             if x[j] <= upperLimitforI:
#                 x.pop(x.index(x[j]))
#                 print(x)
#             else:
#                 j+=1
                
        
#         c +=1
#         print ("station number", c)
#     print("How many stations in total? ", c)

# hackerlandRadioTransmitters(lista, k)






# def compareTriplets(a, b):
#     a_score, b_score = 0, 0
#     # Write your code here
#     for i, j in zip(a, b):
#         if i > j:
#             a_score = a_score + 1
#         elif i < j:
#             b_score = b_score + 1
#     return [a_score, b_score]

# print( type( compareTriplets((1,2,3), (3,2,1)) ) )
