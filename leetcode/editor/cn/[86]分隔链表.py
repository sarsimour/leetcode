
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        this_node = ListNode(0, head)
        small_head, large_head = ListNode(0, None), ListNode(0, None)
        small_pointer, large_pointer = small_head, large_head
        while this_node.next is not None:
            if this_node.next.val < x:
                small_pointer.next = this_node.next
                small_pointer = small_pointer.next
            else:
                large_pointer.next = this_node.next
                large_pointer = large_pointer.next
            this_node = this_node.next
        small_pointer.next = large_head.next
        # 这里是关键，large_pointer可能仍然在原表中有next的node，所以必须手动设置next为None
        large_pointer.next = None
        return small_head.next

# leetcode submit region end(Prohibit modification and deletion)
