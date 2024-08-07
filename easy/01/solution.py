class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        sum: list[int] = []
        
        for i in range(len(nums)):
            
            for j in range(i+1, len(nums)):
                
                if nums[i] + nums[j] == target:
                    sum.append(i)
                    sum.append(j)
                    return sum
        
        return sum