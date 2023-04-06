# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # initialize dummy node
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            # list 1 value == list 2 value
            if list1.val < list2.val:
                # insert it into our tail
                tail.next = list1
                # moving to next item
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            # will update either way
            tail = tail.next

        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next
