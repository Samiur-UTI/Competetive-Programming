def worker(arr):
    answer = 0
    while len(arr) != 0:
        summation = sum(arr)
        average = summation / len(arr)
        arr = [item for item in arr if item < average]
        if len(arr) > 0:
            answer += 1
    print (answer)
testcase = int(input(''))
for i in range(testcase):
    ##length = int(input(''))
    ##No use of length
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    worker(case)

