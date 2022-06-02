x = list(map(int, input().split()))
n = x[0]
q = x[1]
a = list(map(int, input().split()))
total = sum(a)
flagValue = 0
flag = False
for i in range(q):
    t = list(map(int, (input().split())))
    if t[0] == 2:
        total = len(a)*t[1]
        print(total)
        flag = True
        flagValue = t[1]
    else:
        if flag == True:
            total -= flagValue
            total += t[2]
            a[t[1] - 1] = t[2]
            print(total)
        else:
            total -= a[t[1] - 1]
            total += t[2]
            a[t[1] - 1] = t[2]
            print(total) 