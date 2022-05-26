t = int(input(''))
length = int(input(''))
for x in range(t):
    n = input()
    arr = [int(char) for char in n.split()]
    if(len(arr) == length):
        step = int(input())
        o = {}
        p = []
        B = []
        for h in range(step):
            _q = input()
            q_i = [int(char) for char in _q.split()]
            B.append(q_i)
            for item in B:
                if(item[1] == 0):
                    p.append(arr[item[0]-1])
                else:
                    for i in range(item[1]):
                        for i in arr:
                            x = arr.count(i)
                            o[i] = x
                        for j in range(len(arr)):
                            if(arr[j] in o.keys()):
                                arr[j] = o[arr[j]]
        p.append(arr[item[0]-1])
for item in p:
    print(f"result {item}")
        # b = [o[key] if l == int(key) else l for l in arr]     
    
    
        

# # Use the mapped values to transform the array into nth step and return the value based on index
