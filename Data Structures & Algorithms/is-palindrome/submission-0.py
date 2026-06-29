class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean=[]
        for char in s:
            if char.isalnum():
                clean.append(char.lower())
            
        word = "".join(clean)
        return word == word[::-1]
        