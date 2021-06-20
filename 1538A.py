testcase = int(input(''))
for i in range(testcase):
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    if int(array_length) == len(arr):
        max_distance_from_start = case.index(max(case)) + 1
        min_distance_from_start = case.index(min(case)) + 1
        difference = max_distance_from_start - min_distance_from_start
        max_distance_from_end = len(arr) - max_distance_from_start
        min_distance_from_end = len(arr) - min_distance_from_start
        if max_distance_from_start >= max_distance_from_end:
            if min_distance_from_start >= min_distance_from_end:
                lowest = [max_distance_from_end, min_distance_from_end]
                print(max(lowest))
        elif max_distance_from_end >= max_distance_from_start:
            if min_distance_from_end >= min_distance_from_start:
                lowest = [max_distance_from_start, min_distance_from_start]
                print(max(lowest))
        else:
            all_distance = [max_distance_from_start, min_distance_from_start,max_distance_from_end,min_distance_from_end]
            ans1 = min(all_distance)
            index1 = all_distance.index(ans1)
            all_distance.pop(index1)
            ans2 = min(all_distance)
            answer = ans1 + ans2
            print(answer)
                    
        
        

## If lowest two are in the same set then the greater number in that set is the answer, if the lowest two are in different sets then their sum is the answer
