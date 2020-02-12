class Solution:
    def reverseString(self, s: List[str]) -> None:
        """Do not return anything, modify s in-place instead."""
        hardcopy = s[:]
        for i in range(0,len(s)):
            s[i] = hardcopy[-(i+1)]
