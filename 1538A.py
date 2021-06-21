testcase = int(input(''))
for i in range(testcase):
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    if int(array_length) == len(arr):
        set_start = {}
        set_end = {}
        set_start['max_distance'] = case.index(max(case)) + 1
        set_start['min_distance'] = case.index(min(case)) + 1
        set_end['max_distance']= (len(arr) - set_start['max_distance']) + 1
        set_end['min_distance'] = (len(arr) - set_start['min_distance']) + 1
        difference = set_start['max_distance'] - set_start['min_distance']
        all_distance = [set_start['max_distance'], set_start['min_distance'],set_end['max_distance'],set_end['min_distance']]
        ans1 = min(all_distance)
        index1 = all_distance.index(ans1)
        all_distance.pop(index1)
        ans2 = min(all_distance)
        all_distance.insert(index1, ans1)
        maxmin_start = [all_distance[0],all_distance[1]]
        case1 = max(maxmin_start)
        maxmin_end = [all_distance[2],all_distance[3]]
        case2 = max(maxmin_end)
        case3 = ans1 + ans2
        answer = min(case1,case2,case3)
        print(answer)