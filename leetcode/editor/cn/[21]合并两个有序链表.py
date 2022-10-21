
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        import numpy as np
        all_pointers = [list1, list2]
        pre_head = ListNode()
        this_node = pre_head
        while not all([item is None for item in all_pointers]):
            min_val, min_loc = np.inf, -1
            for i, item in enumerate(all_pointers):
                if item is not None and item.val < min_val:
                    min_val, min_loc = item.val, i
            if min_loc > -1:
                this_node.next = all_pointers[min_loc]
                this_node = this_node.next
                all_pointers[min_loc] = all_pointers[min_loc].next
        return pre_head.next





# leetcode submit region end(Prohibit modification and deletion)
