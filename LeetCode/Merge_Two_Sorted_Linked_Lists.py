# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        result_tail = result
        
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                result_tail.next = l1
                l1 = l1.next
            else:
                result_tail.next = l2
                l2 = l2.next
                
            result_tail = result_tail.next
        result_tail.next = l1 or l2
        return result.next
                
