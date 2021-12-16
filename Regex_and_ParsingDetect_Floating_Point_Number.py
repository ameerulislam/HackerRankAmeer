import re

rounds = int(input())
for _ in range(rounds):
    pattern = re.compile(r'(+|-|+.|-.|.)\d+')
    print(pattern.match)
