t = int(input(''))
for x in range(t):
    n = input()
    arr = [int(char) for char in n.split()]
    step = int(input())
    index = int(input())
    # take input of the index and the nth step of transform
    o = {}
    p = []
    for h in range(step):
        for i in arr:
            x = arr.count(i)
            o[i] = x
        print(o)
        for j in range(len(arr)):
            if(arr[j] in o.keys()):
                arr[j] = o[arr[j]]
        p.append(tuple(arr))
    print(p)
        # b = [o[key] if l == int(key) else l for l in arr]     
    
    
        

# # Use the mapped values to transform the array into nth step and return the value based on index
