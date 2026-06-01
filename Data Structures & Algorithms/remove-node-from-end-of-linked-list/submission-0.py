class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        nodes.pop(len(nodes)-n)

        if not nodes: return None

        l = len(nodes)
        for i in range(l-1):
            nodes[i].next = nodes[i + 1]

        nodes[-1].next = None
        return nodes[0]