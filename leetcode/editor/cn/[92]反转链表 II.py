
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
        if left == right:
            return head
        pre_head = ListNode(0, head)
        this_node = pre_head
        loc = 0
        left_end = None
        reverse_start = None
        right_start = None
        while loc <= right + 1:
            if loc < left - 1:
                this_node = this_node.next
            elif loc == left - 1:
                left_end = this_node
                this_node = this_node.next
            elif loc == left:
                reverse_start = this_node
                this_node = this_node.next
            elif loc > left and loc <= right:
                temp_next = this_node.next
                this_node.next = left_end.next
                left_end.next = this_node
                reverse_start.next = temp_next
                this_node = temp_next
            # else:
            #     reverse_start.next = this_node
            loc += 1
        return pre_head.next

        
# leetcode submit region end(Prohibit modification and deletion)
