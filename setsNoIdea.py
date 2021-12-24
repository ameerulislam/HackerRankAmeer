inputs = input().split()
n = inputs[0]
m = inputs[1]
nIntsarray = input().split()
A = set(input().split()) #if set was not used 4 of test cases failes as timeout
B = set(input().split()) #if set was not used 4 of test cases failes as timeout

counter = 0
for i in nIntsarray:
    if i in A:
        counter += 1
    if i in B:
        counter -= 1
print(counter)
