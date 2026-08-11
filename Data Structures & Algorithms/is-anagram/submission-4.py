class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')] += ord(s[i]) - ord('a')
            count[ord(t[i])-ord('a')] -= ord(t[i]) - ord('a')
        
        for value in count:
            if value != 0:
                return False
        return True
        