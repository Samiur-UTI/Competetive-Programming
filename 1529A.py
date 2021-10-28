testcase = int(input())
for i in range(testcase):
<<<<<<< HEAD
    array_length = input('')
    charm = input('')
    arr = [char for char in charm.split()]
    mn = min(arr)
    print(f'this is min {mn}')
    most_occur = arr.count(mn)
    print(f'this is freq {most_occur}')
=======
    array_length = input()
    charm = input()
    arr = [int(char) for char in charm.split()]
    mn = min(arr)
    most_occur = arr.count(mn)
>>>>>>> ad811a279569d1a897def862203511308b1a5be0
    print(len(arr)-most_occur)
    