class Solution:
    def isPalindrome(self, s: str) -> bool:
        p1, p2 = 0, len(s)-1
        while p1 < p2:

            while p1<p2 and not self.check(s[p1]):
                p1 += 1
            while p1<p2 and not self.check(s[p2]):
                p2 -= 1

            if self.get_lower(s[p1]) != self.get_lower(s[p2]):
                return False
            
            p1 += 1
            p2 -= 1
        return True
    
    def check(self, char):
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

    def get_lower(self, char):
        if ord('A') <= ord(char) <= ord('Z'):
            return chr(ord(char) - ord('A') + ord('a'))
        else:
            return char
