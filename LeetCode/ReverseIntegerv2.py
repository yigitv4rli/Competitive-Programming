class Solution:
    def reverse(self, x: int) -> int:
        strVersion = str(x)
        print(strVersion)
        
        if strVersion[0] == "-":
            number = -1 * int(strVersion[-1:0:-1])
        
        else:
            number = int(strVersion[::-1])
            
        
        
        if number > 2**31 -1 or number < -2**31:
            return 0
        else:
            return number
