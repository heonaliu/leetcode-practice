#@param a: takes in int list
#@param b: takes in an int
#@retun: int list of indexes of sum of target

def twoSum(nums, target):
    if (len(nums) == 2):
        if (nums[0] + nums[1] == target):
            return [0,1]


    for i in range(len(nums)):
        goal = target - nums[i]
        
        if (goal in nums and i == nums.index(goal)):
            continue
        if (goal in nums):
            try:
                if (nums.index(goal, nums.index(goal, target+1)+1)):
                    ans = [i, nums.index(goal, target+1)]
                    return ans
            except ValueError:
                ans = [i, nums.index(goal)]
                return (ans)
            
#input of numbers separated by commas
nums = input("").split(",")
nums =  list(map(int, nums))
target = int(input(""))

print(twoSum(nums, target))
