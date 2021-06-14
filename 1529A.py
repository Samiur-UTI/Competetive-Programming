testcase = int(input(''))
def worker(arr):
    iterator = 0
    while iterator < len(arr):
        pass
    iterator += 1
    if iterator <= -1:
        return 0
    else: return iterator
for i in range(testcase):
    ##length = int(input(''))
    ##No use of length
    charm = input('')
    arr = [char for char in charm.split()]
    case = list(map(lambda x: int(x, 10) , arr))
