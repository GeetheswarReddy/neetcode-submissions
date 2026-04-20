class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        h={}
        for i in s:
            h[i]=h.get(i,0)+1
        for i in t:
            if i not in h :
                return False
            h[i]=h[i]-1
            if h[i]<0:
                return False
        for count in h.values():
            if count > 0:
                return False
        return True



        