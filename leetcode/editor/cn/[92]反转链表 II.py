
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        pre_head = ListNode(0, head)
        loc = 0
        left_end = None
        while loc <= right:
            if loc == left - 1:
                left_end = head
            elif loc > left - 1:

            head = head.next
            loc += 1

        
# leetcode submit region end(Prohibit modification and deletion)
