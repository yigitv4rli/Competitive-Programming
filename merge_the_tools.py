def merge_the_tools(string, k):
    queue = []
    len_q = 0
    for item in string:
        len_q += 1
        if item not in queue:
            queue.append(item)
        if len_q == k:
            print(''.join(queue))
            queue = []
            len_q = 0


if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
