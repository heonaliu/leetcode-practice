#@params a: int list
#@params b: int
#returns: an int

def removeElement(nums, val) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        return k

#enter a list separated by commas
l = list(input("").split(","))
l = [int(i) for i in l]

value = int(input(""))
print(removeElement(l, value))
