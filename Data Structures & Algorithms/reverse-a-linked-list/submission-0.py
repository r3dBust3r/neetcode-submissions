# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return None
        stack = []
        while head:
            stack.append(head)
            head = head.next
        stack = stack[::-1]

        for i in range(len(stack) - 1):
            stack[i].next = stack[i + 1]
        
        stack[-1].next = None
        return stack[0]