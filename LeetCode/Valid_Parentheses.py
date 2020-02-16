class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opening = ["(","[","{"]
        closing = [")","]","}"]
        
        for character in s:
            if character in opening:
                stack.append(character)
                
            elif character in closing:
                if len(stack) == 0:
                    return False
                elif opening.index(stack.pop()) != closing.index(character):
                    return False
                
        if len(stack) != 0:
            return False
        return True
