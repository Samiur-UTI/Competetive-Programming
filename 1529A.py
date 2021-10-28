testcase = int(input(''))
for i in range(testcase):
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    mn = min(arr)
    print(f'this is min {mn}')
    most_occur = arr.count(mn)
    print(f'this is freq {most_occur}')
    print(len(arr)-most_occur)
    