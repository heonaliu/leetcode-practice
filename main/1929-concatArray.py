#@params a: int list
#return int list

def getConcatenation(self, nums: List[int]) -> List[int]: #type: ignore
        return nums + nums

givenList = (input("")).split(" ")
givenList = (int(i) for i in givenList)

print(getConcatenation(givenList))

