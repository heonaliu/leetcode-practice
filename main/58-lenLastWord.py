s = input("s: ")

def lengthOfLastWords(s):
        s = s.split(" ")
        for i in range(len(s)-1, -1, -1):
            if s[i].isalpha():
                e = s[i]
                break
        return len(e)
    
print(lengthOfLastWords(s))