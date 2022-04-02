'''
Author: sarsimour
Date: 2022-04-02 17:09:49
LastEditTime: 2022-04-02 17:10:34
LastEditors: sarsimour
Description: 
FilePath: /leetcode/242.有效的字母异位词.py
'''
#
# @lc app=leetcode.cn id=242 lang=python3
#
# [242] 有效的字母异位词
#
# https://leetcode-cn.com/problems/valid-anagram/description/
#
# algorithms
# Easy (65.10%)
# Likes:    542
# Dislikes: 0
# Total Accepted:    389.4K
# Total Submissions: 597.7K
# Testcase Example:  '"anagram"\n"nagaram"'
#
# 给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。
# 
# 注意：若 s 和 t 中每个字符出现的次数都相同，则称 s 和 t 互为字母异位词。
# 
# 
# 
# 示例 1:
# 
# 
# 输入: s = "anagram", t = "nagaram"
# 输出: true
# 
# 
# 示例 2:
# 
# 
# 输入: s = "rat", t = "car"
# 输出: false
# 
# 
# 
# 提示:
# 
# 
# 1 
# s 和 t 仅包含小写字母
# 
# 
# 
# 
# 进阶: 如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import defaultdict
        
        s_dict = defaultdict(int)
        t_dict = defaultdict(int)

        for x in s:
            s_dict[x] += 1
        
        for x in t:
            t_dict[x] += 1

        return s_dict == t_dict
# @lc code=end

