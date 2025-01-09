# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        tail = head
        nodes = []

        while tail:
            nodes.append(tail)
            tail = tail.next

        start, stop = 0, len(nodes) -1

        while start < stop:
            nodes[start].next = nodes[stop]
            start += 1
            if start >= stop:
                break
            nodes[stop].next = nodes[start]
            stop -= 1
        
        nodes[start].next = None