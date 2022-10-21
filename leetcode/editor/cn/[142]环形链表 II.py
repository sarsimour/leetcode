
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        hasCycle = False
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if hasCycle:
            slow = head
            while True:
                if slow == fast:
                    return fast
                slow = slow.next
                fast = fast.next
        else:
            return None

        
# leetcode submit region end(Prohibit modification and deletion)
