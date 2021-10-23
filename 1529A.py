testcase = int(input())
for i in range(testcase):
    array_length = input()
    charm = input()
    arr = [int(char) for char in charm.split()]
    mn = min(arr)
    most_occur = arr.count(mn)
    print(len(arr)-most_occur)
    