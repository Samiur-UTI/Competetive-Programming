test = int(input())
for i in range(test):
    case = input()
    arr = [int(char) for char in case.split()]
    new_arr = sorted(arr)
    largest = new_arr[len(new_arr) - 1]
    ans = []
    i = 0
    if(arr[0]== arr[1] == arr[2]):
        ans = ['1','1','1']
    elif(arr.count(largest)>1):
        while(i < len(arr)):
            if(arr[i] == largest):
                ans.append(str(1))
            else:
                ans.append(str((largest-arr[i])+1))
            i+=1    
    else:
        while(i<len(arr)):
            if(arr[i]<largest):
                ans.append(str((largest-arr[i]) + 1))
            else: 
                ans.append(str(0))
            i+=1
    printer = ' '.join(map(str, ans))
    print(printer)