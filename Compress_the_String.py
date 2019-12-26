string = input()
i = 0 

version = []
while i < len(string):
        
        c = string[i]
        
        j = i + 1 
    
        compressed = [1,int(c)]
    
        while j < len(string):
            if string[j] == c:
                compressed[0] += 1
            else: 
                break
            j += 1

        version.append(str(tuple(compressed)))
        
        i = j
print(" ".join(gene))
