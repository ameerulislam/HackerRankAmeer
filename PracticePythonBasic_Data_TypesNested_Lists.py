if __name__ == '__main__':
    name_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        name_score.append([name,score])
    name_score.sort()
    name_score.sort(key=lambda x: x[1])
    name_score_minValue = name_score[0][1]

    #checking if there are more than one lowest values
    counter = 0
    for i in name_score:
        if i[1] == name_score[0][1]:
            counter += 1
    #Printng the second lowest values
    name_score = name_score[counter:]
    for i in name_score:
        if i[1] == name_score[0][1]:
            print(i[0])
