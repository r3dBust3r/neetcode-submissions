class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for c in s:
            if "a" <= c <= "z" or "A" <= c <= "Z" or "0" <= c <= "9":
                new_s += c.lower()
        
        for i in range(len(new_s)):
            if new_s[i] != new_s[len(new_s) - 1 - i]:
                return False

        return True