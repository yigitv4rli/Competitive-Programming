class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        index = 0
        dic = {}
        length = len(s)
        while index <= length:
            sr = ""
            for char in s[index:]:
                sr += char
                if sr == sr[::-1]:
                    dic[len(sr)] = sr
            index +=1
        if len(s) == 0:
            return ""
        
        maximum = max(dic)
        return dic[maximum]
                
