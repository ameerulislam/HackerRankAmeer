#PracticeInterview Preparation KitWarm-up ChallengesSales by Match
lista = [9, 5, 4, 9, 2, 6, 15, 12, 9, 2]

print(lista.count(9))

unique_stuff =list(set(lista))
print(unique_stuff)
list2 = []
for i in lista:
    list2.append((i, lista.count(i)))

list3 = list(set(list2))
counter = 0
for i in list3:
    if i[1] > 1:
        counter = counter + i[1]//2
print(counter)