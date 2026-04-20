from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        result = [0] * n

        if zero_count > 1:
            return result
       
        elif zero_count == 1:
            for i in range(n):
                if nums[i] == 0:
                    result[i] = product
                else:
                    result[i] = 0
        
        else:
            for i in range(n):
                result[i] = product // nums[i]

        return result
