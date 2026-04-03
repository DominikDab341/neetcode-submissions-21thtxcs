class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.split()
        s = "".join(s)
        pal = ""
        for character in s:
            if character.isdigit():
                pal+=character
            elif character.isalpha():
                pal+=character
        if pal == pal[::-1]:
            return True
        else: 
            return False
        