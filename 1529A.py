def worker(arr):
    summation = sum(arr)
    average = summation / len(arr)
    new_arr = [item for item in arr if item < average]
    print (new_arr)
    # if iterator <= -1:
    #     return 0
    # else: return iterator
testcase = int(input(''))
for i in range(testcase):
    ##length = int(input(''))
    ##No use of length
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    worker(case)

