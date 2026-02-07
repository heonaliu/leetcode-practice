#@param a: takes in int list
#@retun: int list 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]: #type: ignore
        num = int("".join(map(str, digits)))
        num = list(str(num+1))
        num = [int(i) for i in num]
        return num