'''
Author: sarsimour
Date: 2022-04-02 12:54:29
LastEditTime: 2022-04-02 13:13:27
LastEditors: sarsimour
Description: 
FilePath: /leetcode/19.删除链表的倒数第-n-个结点.py
'''
#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第 N 个结点
#
# https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/description/
#
# algorithms
# Medium (43.73%)
# Likes:    1929
# Dislikes: 0
# Total Accepted:    725.5K
# Total Submissions: 1.7M
# Testcase Example:  '[1,2,3,4,5]\n2'
#
# 给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4,5], n = 2
# 输出：[1,2,3,5]
# 
# 
# 示例 2：
# 
# 
# 输入：head = [1], n = 1
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1,2], n = 1
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中结点的数目为 sz
# 1 <= sz <= 30
# 0 <= Node.val <= 100
# 1 <= n <= sz
# 
# 
# 
# 
# 进阶：你能尝试使用一趟扫描实现吗？
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        pre = ListNode()
        pre.next = head
        slow, fast = pre, head
        lag = 1
        while fast.next:
            fast = fast.next
            if lag >= n:
                slow = slow.next
            lag += 1
        # print(slow.val, fast.val)
        slow.next = slow.next.next
        return pre.next
        
            
# @lc code=end

