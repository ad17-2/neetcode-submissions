# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        if not head or not head.next:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        ptr_2, curr = None, slow

        while curr:
            tmp = curr.next
            curr.next = ptr_2
            ptr_2 = curr
            curr = tmp

        first, second = head, ptr_2

        while second.next:
            f_next, s_next = first.next, second.next
            first.next = second
            second.next = f_next
            first, second = f_next, s_next