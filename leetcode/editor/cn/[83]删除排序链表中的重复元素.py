
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow, fast = head, head
        while fast is not None:
            if fast.val > slow.val:
                slow.next = fast
                slow = slow.next
            else:
                slow.next = fast.next
            fast = fast.next
        return head
        
# leetcode submit region end(Prohibit modification and deletion)
