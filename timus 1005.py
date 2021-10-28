length = int(input())
num = input()
arr = [int(item) for item in num.split()]
if(len(arr) == length):
    srt =  sorted(arr)
    last = len(srt)
    while(last != 1):
        diff = abs(srt[last-1] - srt[last-2])
        srt.pop(last-1)
        srt.pop(last-2)
        srt.insert(last-1,diff)
        last -= 1
    print(diff)
        
            