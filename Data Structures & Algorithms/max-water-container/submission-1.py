class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxArea=0
        n=len(heights)
        left=0
        right=n-1
        i=0
        while(left<right):
            height=min(heights[left],heights[right])
            width=(right-left)
            maxArea=max(maxArea,height*width)
            if heights[left]<heights[right]:
                left+=1
            else:
                right-=1
        return maxArea

        
        