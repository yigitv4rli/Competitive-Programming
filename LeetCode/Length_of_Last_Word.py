class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        i = len(s)-1
        length = 0
        while i >= 0:
            if str.isalnum(s[i]):
                length +=1
                i -=1
            else:
                break
        return length
