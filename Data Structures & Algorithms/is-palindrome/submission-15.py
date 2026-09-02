class Solution:
    def isPalindrome(self, s: str) -> bool:
        newStr = ""
        for char in s:
            if char.isalnum():
                newStr += char.lower()
        n = len(newStr)
        left, right = 0, n-1
        while left < right:
            if newStr[left] != newStr[right]:
                return False
            left += 1
            right -= 1
        return True

        
        
        
        