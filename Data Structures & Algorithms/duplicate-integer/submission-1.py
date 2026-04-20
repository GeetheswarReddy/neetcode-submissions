class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        
        for num in nums:
            # If key exists (by checking its value), it's a duplicate
            try:
                if dic[num] >= 0:  # Key exists
                    return True
            except:
                # Key doesn't exist, add it
                dic[num] = 1
                
        return False