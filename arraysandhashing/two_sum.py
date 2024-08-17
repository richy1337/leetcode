class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = set()
        for i in range(len(nums)):
            check = target - nums[i]
            if check in seen:
                return [nums.index(check), i]
            else:
                seen.add(nums[i])


'''
This solution uses a Hash Set for efficient value retrieval.

Initialise a set seen to store all the seen values while iterating through the list of integers.
At each iteration calculate the check integer which is equal to the target - number
Then check if the check integer is within seen
    If so, return the index of check in the list of nums and the current index
    Otherwise, add the value to seen

You will never come across the situation where you have to add a duplicate integer
'''