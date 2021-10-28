t = int(input(''))
for x in range(t):
    n = input()
    arr = [int(char) for char in n.split()]
    # take input of the index and the nth step of transform
    o = {}
    for i in arr:
        x = arr.count(i)
        o[i] = x

# Use the mapped values to transform the array into nth step and return the value based on index

        