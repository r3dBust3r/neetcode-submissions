# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        reordered = []

        l = len(nodes)
        for i in range(l // 2):
            reordered.append(nodes[i])
            reordered.append(nodes[l - 1 - i])

        if l % 2 == 1:
            reordered.append(nodes[l // 2])


        for i in range(l - 1):
            reordered[i].next = reordered[i + 1]

        reordered[-1].next = None