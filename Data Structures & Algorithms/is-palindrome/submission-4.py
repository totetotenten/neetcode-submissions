class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()   
        s_alpha = "".join(char.lower() for char in s if char.isalnum())
        length = len(s_alpha)
        for i in range(length//2):
                if s_alpha[i] != s_alpha[length-i-1]:
                    return False
        return True