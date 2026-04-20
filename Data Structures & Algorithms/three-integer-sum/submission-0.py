class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        arr = []
        
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            lo, high = i + 1, len(nums) - 1
            
            while lo < high:
                su = nums[i] + nums[lo] + nums[high]
                if su == 0:
                    arr.append([nums[i], nums[lo], nums[high]])
                    while lo < high and nums[lo] == nums[lo + 1]:
                        lo += 1
                    while lo < high and nums[high] == nums[high - 1]:
                        high -= 1
                    lo += 1
                    high -= 1
                elif su < 0:
                    lo += 1
                else:
                    high -= 1
        
        return arr
