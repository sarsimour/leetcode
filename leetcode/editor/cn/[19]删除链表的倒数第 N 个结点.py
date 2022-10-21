
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        pre_head = ListNode(0, head)
        pre_node = pre_head
        next_node = pre_head
        for i in range(n):
            next_node = next_node.next
        while next_node.next is not None:
            pre_node = pre_node.next
            next_node = next_node.next
        pre_node.next = pre_node.next.next
        return pre_head.next

        
# leetcode submit region end(Prohibit modification and deletion)
