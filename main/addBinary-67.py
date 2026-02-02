a = input("a: ")
b = input("b: ")

zero = "0"
diff = abs(len(b)-len(a))

if (diff != 0):
    zero *= diff
    if (len(a)<len(b)): #a is smaller than b
        a = zero + a
    else: #b is smaller than a
        b = zero + b

sum = 0
carry = False
answer = ""

for i in range(len(a)-1, -1, -1):
    sum = int(a[i])+int(b[i])
    
    if (carry):
        sum+=1

    if (sum == 0): #0+0+0
        answer = "0" + answer
    
    if (sum == 1): #1+0+0 || 0+1+0 || 0+0+1
        answer = "1" + answer
        carry = False #if carry is positive

    if (sum == 2): #1+1+0
        answer = "0" + answer 
        carry = True

    if (sum == 3): #1+1+1
        answer = "1" + answer

#first digit
if (carry):
    answer = "1" + answer

print(answer)