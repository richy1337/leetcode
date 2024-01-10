def containsDuplicate(nums):
        
        duplicate = False
        seen = {}
        for i in range(len(nums)):
            if nums[i] in seen == False:
                seen[i] += nums[i]
                print(seen[i])
            else:
                duplicate = True
     
        return duplicate
        
nums = [1,2,3,4]
print(containsDuplicate(nums))x