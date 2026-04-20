class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic={}
        for i in nums:
            num=0
            if i not in dic:
                dic[i]=num
            else:
                dic[i]+=1

        for value in dic.values():
            if(value!=0):
                return True
        return False

         