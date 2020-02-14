class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = len(s)
        i = 0 
        result = 0
        while i < length-1:
            stack = [s[i]]
            j = i+1
            while j < length:
                if s[j] not in stack:
                    stack.append(s[j])
                    j+=1
                else:       
                    break
            result = max(result, len(stack))
            i+=1
        if length == 0:
            return 0
        elif length == 1:
            return 1
        else:
            return result
