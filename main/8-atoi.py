s = input("s: ")


def myAtoi(s):
    
    if (len(s)==0):
        return 0
    digitOrSignFound = False
    i = 0
    ans = ""
    while (not digitOrSignFound):

        if (s[i] != " " and (s[i].isdigit() or s[i] == "+" or  s[i] == "-")):
            digitOrSignFound = True
            break
        if (i==len(s)-1 or not s[i].isdigit() and s[i] != " " ): #reached end of string
            return 0 
        i+=1

    s = s[i:]
    sign = False
    noDigits = True
    digitDefined = False

    neg = 1
    if (s[0]=="-"):
        num = s[1:]
        neg = -1
        sign = True
    elif (s[0] == "+"):
        num = s[1:]
        sign = True
    else:
        num = s

    for i in range(0, len(num)):
        
        if (num[i] == "0" and sign and not digitDefined):
            continue
        
        if (not num[i].isdigit() or num[i] == "-" or num[i] == "+" ): 
            break
        
        if (num[i].isdigit() and num[i] != "0"):
            digitDefined = True
        ans = ans + num[i]

    if (len(ans)>0):
        noDigits = False
        
    if(noDigits == False and int(ans).bit_length() == 32):
        if (int(ans) >= (2**31)):
            if (neg == 1):
                return neg*(2**31)-1
            else:
                return neg*(2**31)
        return neg * (2**31)
    elif (noDigits == False and int(ans).bit_length()>32):
        if (neg == -1):
            return neg * (2**31)
        else:
            return neg * (2**31) -1
    
    if(noDigits == True):
        return 0
    else:
        if (neg == -1):
            
            return int("-" + ans)
        else:
            return int(ans)

print(myAtoi(s))