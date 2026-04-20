'''class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash={}
        l=[]
        for st in strs:
            hash_1={}
            for i in st:
                hash_1[i]=hash_1.get(i,1)+1
            hash[st]=hash_1
        for st in strs:
            l1=[]
            if st in hash:'''
                
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res=defaultdict(list)
        for st in strs:
            count=[0]*26
            for i in st:
                count[ord(i)-ord('a')]+=1
            res[tuple(count)].append(st)
        return res.values()
        
            
        