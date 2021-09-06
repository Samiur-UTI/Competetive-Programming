testcase = int(input(''))
for i in range(testcase):
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    obj={}
    for item in arr:
        obj[item] = 0
    for item in arr:
        obj[item] += 1
    max_value = max(obj,key=obj.get)
    most_occur = arr.count(max_value)
    print(len(arr)-most_occur)
    