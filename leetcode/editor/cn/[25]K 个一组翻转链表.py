
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        left, right = 1, k
        if left >= right:
            return head
        pre_head = ListNode(0, head)
        sec_end = pre_head
        this_node = pre_head
        loc = 0
        real_loc = 0
        left_end = None
        reverse_start = None
        right_start = None
        residual = False
        while this_node is not None or not residual:

            if loc == left - 1:
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
                if loc == right:
                    loc = 0
                    left_end = reverse_start
                    sec_end = left_end
            # else:
            #     reverse_start.next = this_node
            if this_node is None and not residual and loc < right:
                residual = True
                loc = 0
                this_node = sec_end
                # print(loc, real_loc, left, right)
                # print(pre_head.next)
                # print(this_node)
                continue
            loc += 1
            real_loc += 1
            # print(loc, real_loc, left, right)
            # print(pre_head.next)
            # print(this_node)
        return pre_head.next

# leetcode submit region end(Prohibit modification and deletion)
