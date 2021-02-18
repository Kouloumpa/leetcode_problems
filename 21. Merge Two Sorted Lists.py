#Time Complexity: O(len(l1) + len(l2))
#Space Complexity: O(len(l1) + len(l2))
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        if not l1 and not l2:
            return ListNode(0).next
        
        output = []
        
        while l1 and l2:
                
            if l1.val <= l2.val:
                output.append(l1)
                l1 = l1.next
            else:
                output.append(l2)
                l2 = l2.next
                
        while l1:
            output.append(l1)
            l1 = l1.next
            
        while l2:
            output.append(l2)
            l2 = l2.next
            
        for i in range(len(output)-1):
            output[i].next = output[i+1]
        output[-1].next = None
            
        return output[0]