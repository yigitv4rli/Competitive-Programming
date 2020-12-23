# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def makeReverse(r, n):
    i = 0
    
    prev = None
    
    while i < n:
        temp = r.next
        r.next = prev
        prev = r
        r = temp
        i+=1
        
    return prev
    
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        p1 = head
        length = 0
        
        while p1:
            p1 = p1.next
            length+=1
            
        if length == 1:
            return True
        
        """1 2 3 4"""
        p1 = head
        p2 = head
        if length % 2 == 0:
            for i in range(length//2):
                p2 = p2.next
            reverseHead = makeReverse(head, length//2)

        
        else:
            """1 2 3 4 5"""
            for i in range(length//2 +1):
                p2 = p2.next
            reverseHead = makeReverse(head, length // 2)

        while p2:
            if p2.val != reverseHead.val:
                return False
            p2 = p2.next
            reverseHead = reverseHead.next
        return True
                
                
                
                
                
                
                
