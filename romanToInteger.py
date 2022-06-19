def romanToInteger(s):
    obj={
            "I":1,
            "IV":4,
            "V":5,
            "IX":9,
            "X":10,
            "XL":40,
            "L":50,
            "XC":90,
            "C":100,
            "CD":400,
            "D":500,
            "CM":900,
            "M":1000,
        }
    num = 0
    for i in range(len(s)):
        if (s[i] == 'V' or s[i] == 'X') and i != 0:
            if(s[i-1] == 'I'):
                print("FIRST",i)
                x = str(s[i-1]) + str(s[i])
                num -= obj["I"]
                num += obj[x]
            else:
                num += obj[s[i]]
                print("FIRST",num)
        elif (s[i] == 'L' or s[i] == 'C') and i != 0:
            if(s[i-1] == 'X'):
                x = str(s[i-1]) + str(s[i])
                num -= obj["X"]
                num += obj[x]
            else:
                num += obj[s[i]]
        elif (s[i] == 'D' or s[i] == 'M') and i != 0:
            if(s[i-1] == 'C'):
                x = str(s[i-1]) + str(s[i])
                num -= obj["C"]
                num += obj[x]
            else:
                num += obj[s[i]]
        else:
            print("EKHANE",num)
            num += obj[s[i]]
    return num            

print(romanToInteger("VII"))