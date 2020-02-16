class Solution:
    def myAtoi(self, string: str) -> int:
        string = string.strip()
        
        if string == "":
            return 0
        
        if string[0] == "-" or string[0] == "+":
            sign = string[0]
            number = ""
            
            for character in string[1:]:
                if str.isdigit(character) == True:
                    number += character
                else:
                    break
            number = sign + number
            
        else:
            number = ""
            for character in string:
                if str.isdigit(character) == True:
                    number += character
                else:
                    break
            
        if number == "" or number == "+" or number == "-":
            return 0
        
        elif 2**31 - 1 >= int(number) >= -2**31:
            return int(number)
        
        else:
            if int(number) > 2**31 - 1:
                return 2**31 - 1 
            elif int(number) < -2**31:
                return -2**31  
