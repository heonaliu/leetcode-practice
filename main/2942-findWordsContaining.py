givenList = (input("")).split(" ") #seperated by space
character = input("x: ")

#returns a list of int
def findWordsContaining(words, x):
        index = []
        for i in range(len(words)):

            if x in words[i]:
                index.append(i)
        return index
    
print(findWordsContaining(givenList, character))