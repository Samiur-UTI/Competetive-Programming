testcase = int(input(''))
for i in range(testcase):
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    if int(array_length) == len(arr):
        max_distance_from_start = case.index(max(case)) + 1
        min_distance_from_start = case.index(min(case)) + 1
        start_pair = (max_distance_from_start,min_distance_from_start)
        max_distance_from_end = len(arr) - max_distance_from_start
        min_distance_from_end = len(arr) - min_distance_from_start
        end_pair = (max_distance_from_end,min_distance_from_end)
        if (sum(start_pair) > sum(end_pair)):
            print(max(end_pair))
        elif(sum(end_pair) > sum(start_pair)):
            print(max(start_pair))
        else: print(max(start_pair))        