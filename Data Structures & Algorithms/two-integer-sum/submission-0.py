class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash={}
        for i in range(len(nums)):
            k=target-nums[i]
            if k in hash:
                j=hash[k]
                return [j,i]
            hash[nums[i]]=i
        return 0
        
        