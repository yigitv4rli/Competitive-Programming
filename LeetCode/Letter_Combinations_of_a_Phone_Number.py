class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dic = {'2': ['a', 'b', 'c'],
               '3': ['d', 'e', 'f'],
               '4': ['g', 'h', 'i'],
               '5': ['j', 'k', 'l'],
               '6': ['m', 'n', 'o'],
               '7': ['p', 'q', 'r', 's'],
               '8': ['t', 'u', 'v'],
               '9': ['w', 'x', 'y', 'z']}
        
        result = []
        def helperLetterComb(comb, nextDigits):
            if len(nextDigits) == 0:
                result.append(comb)
            else:
                for letter in dic[nextDigits[0]]:
                    helperLetterComb(comb + letter, nextDigits[1:])
                    
        if digits:
            helperLetterComb("", digits)
        return result
