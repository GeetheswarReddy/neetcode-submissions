class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_t={}
        
        for i in range(len(nums)):
            left=target-nums[i]
            if left in hash_t:
                return[hash_t[left],i]
            
            hash_t[nums[i]]=i
        