class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_palind = ""
        for char in s:
            if char.isalnum():
                s_palind += char.lower()
        
        length = len(s_palind)
        for i in range(length//2):
            if s_palind[i] != s_palind[length-i-1]:
                return False
        return True


        