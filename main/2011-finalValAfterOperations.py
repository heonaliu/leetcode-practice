s = input("s: ").split(" ")
#operations[i] will be either "++X", "X++", "--X", or "X--"

#returns an int
def finalValueAfterOperations(operations):
        value = 0
        for i in range(len(operations)):
            if (operations[i][0]=="-" or operations[i][-1]=="-"):
                value -=1
            elif (operations[i][0]=="+" or operations[i][-1] =="+"):
                value +=1
        return value
    
print(finalValueAfterOperations(s))