import itertools
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    list_x = list(range( 0 , x+1))
    list_y = list(range( 0 , y+1))
    list_z = list(range( 0 , z+1))
    # print(list_x)
    # print(list_y)
    # print(list_z)

    product = itertools.product(list_x,list_y, list_z)
    product = list(product)

    result = [list(x) for x in product if sum(x)!=n]
    print(result)