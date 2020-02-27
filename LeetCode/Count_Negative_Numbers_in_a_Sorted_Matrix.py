class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def flatten(lst):
            flat_list = []
            queue = lst
            while(queue):
                first = queue[0] # dequeue
                queue = queue[1:]
                if ( type(first) == list ):
                    queue += first # enqueue
                else:
                    flat_list += [first]
            return flat_list
        
        result = sorted(flatten(grid))
        
        count = 0
        for i in range(0,len(result)):
            if result[i] < 0:
                count +=1
            else:
                break
        return count
                
