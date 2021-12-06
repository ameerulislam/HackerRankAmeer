import itertools
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
   
    permutations = itertools.permutations([list(range(0,x+1)), list(range(0,y+1)), list(range(0,z+1))], 3)
    
    permutations = list(permutations)
    print(permutations)

    thelist = [i for i in permutations if sum(i)!=n]
    print(thelist)