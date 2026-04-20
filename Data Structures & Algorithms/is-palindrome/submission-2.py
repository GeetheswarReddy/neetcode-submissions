class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = []
        s = s.lower()
        for char in s:
            if char.isalnum():
                filtered.append(char)
        y = ''.join(filtered)
        i, j = 0, len(y) - 1
        while i <= j:
            if y[i] != y[j]:
                return False
            i += 1
            j -= 1
        return True
