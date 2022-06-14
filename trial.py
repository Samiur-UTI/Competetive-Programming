def weirdAverage(arr):
    summation = sum(arr)
    average = summation / len(arr)
    deciCheck = str(average).split('.')[1]
    if(int(deciCheck) == 0):
        print(str(average).split('.')[0])
    elif average == 0:
        print(average)
    else:
        print("%.3f" % average)
weirdAverage([6,-6])