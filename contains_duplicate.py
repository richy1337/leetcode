class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        duplicate = False
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)

        return False
    
"""
This solution uses a Hash Set to solve the problem in O(N) time

Initialise a set 'Seen' to store the seen integers while iterating through the array of numbers
Afterwards, iterate through the numbers of the given array and check if the number exists within the 'Seen' set. Checking takes O(!) time
If it does exist, it means that there is a duplicate, if not, it means there is no duplicate.
"""