class Solution:
    def isPalindrome(self, s: str) -> bool:
        def is_alpha(c):
            if ord(c) >= 65 and ord(c) <= 90 or ord(c) >= 97 and ord(c) <= 122 or ord(c) >= 48 and ord(c) <= 57:
                return True
            return False

        i = 0
        j = len(s) - 1
        while i <= j:
            while i <= j and not is_alpha(s[i]):
                i+=1
            while i <= j and not is_alpha(s[j]):
                j-=1
            if i > j:
                break
            if is_alpha(s[i]) and is_alpha(s[j]):
                if s[i].lower() != s[j].lower():
                    print(s[i])
                    print(s[j])
                    return False
                i+=1
                j-=1
        return True
        