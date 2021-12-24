n = int(input())
s = set(map(int, input().split()))
N = int(input())
for _ in range(N):
    operations = input().split()
    if operations[0] == 'pop':
        s.pop()
    elif operations[0] == 'remove':
        s.remove(int(operations[1]))
    elif operations[0] == 'discard':
        s.discard(int(operations[1]))
print(sum(s))

# for _ in range(N):
#     operations = input().split()
#     if operations[0]== 'pop':
#         s.pop()
#     elif operations[0]== 'remove':
#         s.remove(int(operations[1]))
#     elif operations[0]== 'discard':
#         s.discard(int(operations[1]))
# print(sum(s))


# M = input()
# A = set(input().split())
# N = input()
# B = set(input().split())
# union = (A).union(B)
# intersect = (A).intersection(B)
# thediffewewant = (union).difference(intersect)
# thediffewewant = [ int(x) for x in thediffewewant]
# thediffewewant = sorted(thediffewewant)
# print(thediffewewant)
# for i in thediffewewant:
#     print(i)



# def average(array):
#     return round( sum(set(array))/len(list(set(array))), 3 )

# if __name__ == '__main__':
#     n = int(input())
#     arr = list(map(int, input().split()))
#     result = average(arr)
#     print(result)


# def count_substring(string, sub_string):
#     indexes = []
#     x=0
#     for _ in string:
#         lolwa = string.find(sub_string, x)
#         indexes.append(lolwa)
#         x=x+1
#         # print (x, lolwa, len(indexes))
    
#     return len([x for x in sorted(set(indexes)) if x>=0])


#     return 
# if __name__ == '__main__':
#     string = input().strip()
#     sub_string = input().strip()
    
#     count = count_substring(string, sub_string)
#     print(count)




# def mutate_string(string, position, character):
#     # string = list(string)
#     return string[:position]+character+string[position:]

# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# def split_and_join(line):
#     # line = line.split()
#     return '-'.join(line)

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)   
#     print(result)



# def print_full_name(first, last):
#     print("Hello {} {}! You just delved into python.".format(first, last))
# if __name__ == '__main__':
#     first_name = input()
#     last_name = input()
#     print_full_name(first_name, last_name)


#swap_case

# def swap_case(s):
#     return s.swapcase()

# if __name__ == '__main__':
#     s = input()
#     result = swap_case(s)
#     print(result)