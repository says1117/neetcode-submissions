class Solution:
    def isPalindrome(self, s: str) -> bool:
        newS = ''.join(char for char in s if char.isalnum())
        newS = newS.lower()
        return newS == newS[::-1]
        