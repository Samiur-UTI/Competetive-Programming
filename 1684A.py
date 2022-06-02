t = int(input())
for i in range(t):
    arr = []
    n = str(input())
    for i in range(len(n)):
        arr.append(int(n[i]))
    print(min(arr))