class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        track=[[] for i in range(len(nums)+1)]
        count={}
        for i in nums:
            count[i]=count.get(i,0)+1

        for i,j in count.items():
            track[j].append(i)
        res=[]
        for i in range(len(track)-1,0,-1):
            for j in track[i]:
                res.append(j) 
                if len(res)==k:
                    return res       