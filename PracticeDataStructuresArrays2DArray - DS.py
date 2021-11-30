list2d = [[1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [1, 1, 1, 0, 0, 0],
            [0, 0, 2, 4, 4, 0],
            [0, 0, 0, 2, 0, 0],
            [0, 0, 1, 2, 4, 0]]
        
def squaremetrix(arr):
    listrows = len(arr)
    listcols = len(arr[0])
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
        print("matrix shape ",matrixShape)
        

glasshours(list2d)