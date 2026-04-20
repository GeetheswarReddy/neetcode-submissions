class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_t={}
        for i in nums:
            hash_t[i]=hash_t.get(i,0)+1

            if hash_t[i]>1:
                return True
        return False

        
