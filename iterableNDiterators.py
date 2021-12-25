#String Validations UNSOLVED PROBLEM
if __name__ == '__main__':
    s = input()
    binaryfns = ["isalnum()", "isalpha()", "isdigit()", "islower()", "isupper()"]
    for _ in range(len(binaryfns)):
        print( any( [i+"."+binaryfns for i in s  ] ) ) 

# #itertools
# from itertools import combinations
# N = int(input())
# letters_lower = input().split()
# K = int(input())
# combos = list(combinations(letters_lower, K))1
# counter = 0
# for i in combos:
#     if "a" in i:
#         counter = counter + 1
# print(round(counter/len(combos), 3))