
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        back_head = ListNode(head.val, None)
        while head.next is not None:
            this_node = back_head
            back_head = ListNode(head.next.val, this_node)
            head = head.next

        return back_head
        
# leetcode submit region end(Prohibit modification and deletion)
