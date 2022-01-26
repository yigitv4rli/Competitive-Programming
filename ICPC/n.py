# Credits: https://github.com/yesiltepe-hidir/
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

def solve(a, b, n):
    if a[0] < b[0]:
        return -1

    index = 0
    res = 0
    while index < n:
        # print("index:", index)

        if a[index] >= b[index]:
            a[index] -= b[index]
            # print("res:", res)
            # print("A:", a)
            # print("B:", b)
            # print("-"*10)
        
        else:
            remained = b[index] - a[index]
            back_index = index - 1
            while back_index >= 0:
                scale = 2 ** (index - back_index)

                if a[back_index]:
                    if a[back_index] * scale >= remained:

                        for i in range(index - 1, back_index - 1, -1):
                            remained = remained // 2 + (remained % 2 != 0)
                            if i != back_index:
                                a[i] = remained
                                if i != index - 1:
                                    a[i + 1] = (a[i] * 2) - a[i + 1]
                                else:
                                    a[i + 1] += (a[i] * 2)
                            
                            else:
                                a[back_index] -= remained
                                if index - back_index != 1:
                                    a[i + 1] = remained * 2 - a[i + 1]
                                else:
                                    a[index] += 2 * remained
                                
                            # print("A:", a)
                            res += remained
                        a[index] -= b[index]
                        # print("res:", res)
                        # print("A:", a)
                        # print("B:", b)
                        # print("-"*10)
                        break
                    else:
                        res += a[back_index] * (scale - 1)
                        a[index] += a[back_index] * scale
                        a[back_index] = 0
                        remained = b[index] - a[index]
                        # print("res:", res)
                        # print("A:", a)
                        # print("B:", b)
                        # print("-"*10)

                back_index -= 1
            if back_index == -1:
                return -1
        index += 1
    return res


print(solve(a, b, n+1))
