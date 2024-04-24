from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return

        slow = head
        fast = head.next.next
        while head and head.next:
            slow = slow.next
            fast = fast.next.next

        slow.next = slow.next.next
        return head