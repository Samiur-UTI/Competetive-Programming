def consequetiveMedian(arr):
    ans = ''
    window = arr[0]
    arr.pop(0)
    length = len(arr)
    for i in range(length):
        temp = []
        if(window-1 > i):
            for j in range(i):
                temp.append(arr[j])
            if(i == 0):
                median = str(arr[i]) + str(arr[i])
                ans += median
            elif(len(temp) % 2 != 0):
                median = str(arr[j]) + str(temp[len(temp)//2])
                ans += median
            else:
                median = str(
                    arr[j]) + str((temp[len(temp)//2] + temp[len(temp)//2 + 1]) / 2)
                ans += median
            temp = []
        else:
            start = i - (window-1)
            for j in range(start, i+1):
                temp.append(arr[j])
                if(i ==0):
                    median = str(arr[i]) + str(arr[i])
                    ans += median
                elif(len(temp) % 2 != 0):
                    median =  str(arr[j]) + str(temp[len(temp)//2])
                    ans += median
                else:
                    median = str(arr[j]) + str((temp[len(temp)//2] + temp[len(temp)//2 +1]) / 2)
                    ans += median
                temp = []
    return ans


print(consequetiveMedian([1,2,4]))