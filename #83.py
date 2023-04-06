# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # initialize cur variable to = first node aka head
        cur = head
        # while current
        while cur:
            # check if next node is the same value
            while cur.next and cur.next.val == cur.val:
                # deletes node
                cur.next = cur.next.next
            # current node is next node now
            cur = cur.next
        return head
