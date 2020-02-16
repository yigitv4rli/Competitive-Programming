class Solution:
    def reverse(self, x: int) -> int:
            def overflow(x):
                if x >= 2**31-1 or x <= -2**31:
                    return True
                else:
                    return False
                
            def zero_deleter(number):
                result = list(number)
                for i in range(0,len(number)):
                    if number[i] != 0:
                        break
                    else:
                        result = result[i+1:]
                return "".join(result)

            if x == 0:
                return 0
            
            if overflow(x) == True:
                return 0
            elif x < 0:
                x = zero_deleter(str(x)[1:])
                x = zero_deleter(x[::-1])
                x = int("-" + x)
                
                if overflow(x) == True:
                    return 0
                else:
                    return x
            else:
                x = zero_deleter(str(x))
                x = int(zero_deleter(x[::-1]))
                
                if overflow(x) == True:
                    return 0
                else:
                    return x               
