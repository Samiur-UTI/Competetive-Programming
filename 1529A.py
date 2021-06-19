import random
def sequenceMaker(arr):
    counter = 0
    while len(arr) - counter > 0:
        subseq = random.sample(arr,len(arr)- counter)
        worker(subseq)
        counter += 1
def worker(arr):
    answer = 0
    print(f'this is before {arr}')
    while len(arr) != 0:
        summation = sum(arr)
        average = summation / len(arr)
        arr = [item for item in arr if item < average]
        print(f'this is after {arr}')
        if len(arr) > 0:
            answer += 1
testcase = int(input(''))
for i in range(testcase):
    ##length = int(input(''))
    ##No use of length
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
    sequenceMaker(case)

