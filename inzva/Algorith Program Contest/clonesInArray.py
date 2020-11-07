from collections import Counter 
  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0][0] 
    
    
N = int(input())
numbers = list(map(int, input().strip().split()))

    
mF = most_frequent(numbers)
print(N - numbers.count(mF))