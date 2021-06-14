testcase = int(input(''))
for i in range(testcase):
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    max1 = max(case)
    index = case.index(max1)
    case.remove(max1)
    max2 = max(case)
    case.insert(index,max1)
    winners = []
    if(case[0] > case[1]):
        winners.append(case[0])
    else:
        winners.append(case[1])
    if(case[2] > case[3]):
        winners.append(case[2])
    else:
        winners.append(case[3])
    if ((winners[0] == max1 or winners[0] == max2) and (winners[1] == max1 or winners[1] == max2)):
        print('YES')
    else: print('NO')
