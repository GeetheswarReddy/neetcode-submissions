class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''hash, use a for loop for keys and check for hash[key+1],not optimal
        and keep track of count'''
        #dont care about duplicates in this so set is used(trying)
        if nums==[]:
            return 0
        nums=set(nums)
        los=0
        for num in nums:
            if num-1 not in nums:
                los1=0
                while True:
                    if num+1 in nums:
                        los1+=1
                        num+=1
                    else:
                        break
                if los1>los:
                    los=los1
        return los+1
                    