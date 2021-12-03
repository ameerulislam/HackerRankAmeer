import itertools
# 6 X 6 Metrics
list2d = [[1, 2, 3, 4, 5, 6],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]
# check if the metrics is square oterwise we're not playing the glass game, we might be able to but probably square is easier        
def squaremetrix(arr):
    listrows = len(arr) #number of rows
    listcols = len(arr[0]) #number of columns selecting the first row and counting it's 
    for i in arr:
        if len(i) != listcols or listcols !=listrows and i == arr[-1]:
            return "list is not a square"
        elif len(i) == listcols and i == arr[-1]:
            # print("list is a square")
            return "list is a square", listrows , listcols
        else:
            pass
    
isitsqare = squaremetrix(list2d)

def glasshours(arr):
    if squaremetrix(list2d)[0] == 'list is a square':
        matrixShape = [squaremetrix(list2d)[1] , squaremetrix(list2d)[1]]
        # print("matrix shape ",matrixShape)
        for i in arr:
            # lengthofi = len(i)
            # howmanyheads = (lengthofi/3) + 2 #length of row divide by head size + 2
            combinations = itertools.combinations(i, 3)
            print(list(combinations))
                     

glasshours(list2d)