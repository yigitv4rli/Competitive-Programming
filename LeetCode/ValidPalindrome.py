class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if len(s) == 0:
            return True
        
        alphanumVersion = ""
        
        for char in s:
            if char.isalnum() == True:
                alphanumVersion+= char.lower()
                    
        if alphanumVersion == alphanumVersion[::-1]:
            return True
        else:
            return False
    
