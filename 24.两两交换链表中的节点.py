'''
Author: sarsimour
Date: 2022-03-29 16:31:20
LastEditTime: 2022-03-29 17:14:44
LastEditors: sarsimour
Description: 
FilePath: /leetcode/24.两两交换链表中的节点.py
'''
#
# @lc app=leetcode.cn id=24 lang=python3
#
# [24] 两两交换链表中的节点
#
# https://leetcode-cn.com/problems/swap-nodes-in-pairs/description/
#
# algorithms
# Medium (70.68%)
# Likes:    1318
# Dislikes: 0
# Total Accepted:    409.1K
# Total Submissions: 578.6K
# Testcase Example:  '[1,2,3,4]'
#
# 给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。
# 
# 
# 
# 示例 1：
# 
# 
# 输入：head = [1,2,3,4]
# 输出：[2,1,4,3]
# 
# 
# 示例 2：
# 
# 
# 输入：head = []
# 输出：[]
# 
# 
# 示例 3：
# 
# 
# 输入：head = [1]
# 输出：[1]
# 
# 
# 
# 
# 提示：
# 
# 
# 链表中节点的数目在范围 [0, 100] 内
# 0 <= Node.val <= 100
# 
# 
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(next=head)
        pre = res
        while pre.next and pre.next.next:
            temp, post = pre.next, pre.next.next
            temp.next = post.next
            post.next = temp
            pre.next = post
            pre = pre.next.next
        return res.next
            
        
            
# @lc code=end

