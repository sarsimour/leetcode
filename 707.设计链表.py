'''
Author: sarsimour
Date: 2022-03-22 16:09:40
LastEditTime: 2022-03-23 13:29:35
LastEditors: sarsimour
Description: 
FilePath: /leetcode/707.设计链表.py
'''
#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#

# @lc code=start
class MyLinkedList:

    def __init__(self):
        self._head = Node(0)  # 虚拟头部节点
        self._count = 0  # 添加的节点数

    def get(self, index: int) -> int:
        if index < 0 or index >= self._count:
            return -1
        node_ = self._head
        for _ in range(index+1):
            node_ = node_.next
        return node_.val


    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)


    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self._count, val)


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self._count:
            return
        self._count += 1
        pre_node, next_node = None, self._head
        for _ in range(index+1):
            pre_node, next_node = next_node, next_node.next
        pre_node.next = Node(val)
        pre_node.next.next = next_node


    def deleteAtIndex(self, index: int) -> None:
        if 0 <= index < self._count:
            self._count -= 1
            pre_node, next_node = None, self._head
            for _ in range(index+1):
                pre_node, next_node = next_node, next_node.next
            pre_node.next = next_node.next


class Node:
    
    def __init__(self, val):
        self.val = val
        self.next = next

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end

