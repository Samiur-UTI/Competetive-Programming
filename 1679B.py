x = list(map(int, input().split()))
n = x[0]
q = x[1]
a = list(map(int, input().split()))
sum = sum(a)
for i in range(q):
    t = list(map(int, (input().split())))
    if t[0] == 2:
        print(len(a)*t[1])
    else:
        temp = a[t[1] - 1]
        val = t[2]
        a[t[1] - 1] = t[2]
        if temp > val:
            print(sum-(temp - val))
        elif temp < val:
            print(sum+(val - temp))
        else:
            print(sum)