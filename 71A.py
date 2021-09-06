testcase = int(input(''))
for i in range(testcase):
    input_string = input('')
    if len(input_string) > 10:
        arr = [char for char in input_string]
        first = arr[0]
        last = arr[len(arr)-1]
        arr.pop(0)
        arr.pop(len(arr)-1)
        length = len(arr)
        print(f'{first}{length}{last}')
    else: print(input_string)