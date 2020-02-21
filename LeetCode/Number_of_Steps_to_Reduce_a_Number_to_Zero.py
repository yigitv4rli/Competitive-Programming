class Solution:
    def numberOfSteps (self, num: int) -> int:
        step = 0
        while num > 0:
            if num % 2 == 1:
                num -=1
            else:
                num /=2
            step +=1
        return step
