import numpy

def productExceptSelf(nums):
    """         
    :type nums: List[int]5-0p00p
    :rtype: List[int]
    """
    prod = [1] * len(nums)
    num = 1
    for i in range(len(nums)):
        prod[i] = num
        num *= nums[i]

    num = 1
    for i in range(len(nums)-1, -1, -1):
        prod[i] *= num
        num *= nums[i]
    
    return prod