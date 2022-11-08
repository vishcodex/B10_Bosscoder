


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head #slow and fast pointers
        while fast and fast.next: #while not at the end of the list
            slow = slow.next #slow moves forward by 1
            fast = fast.next.next #fast moves forward by 2
            if slow == fast: #if they are the same then we must have a cycle!
                break
        else:
            return None

        while head != slow:
            head, slow = head.next, slow.next
        return head