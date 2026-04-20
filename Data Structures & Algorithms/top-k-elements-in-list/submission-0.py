class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hash_1={}
        for i in nums:
            hash_1[i]=hash_1.get(i,0)+1
        sorted_1=list(sorted(hash_1.items(), key= lambda item:item[1],reverse=True))
        lis=[]
        for i in range(k):
            lis.append(sorted_1[i][0])
        return lis


        