'''
Author: sarsimour
Date: 2022-04-02 17:19:47
LastEditTime: 2022-04-02 17:22:40
LastEditors: sarsimour
Description: 
FilePath: /leetcode/1002.查找共用字符.py
'''
#
# @lc app=leetcode.cn id=1002 lang=python3
#
# [1002] 查找共用字符
#
# https://leetcode-cn.com/problems/find-common-characters/description/
#
# algorithms
# Easy (72.55%)
# Likes:    266
# Dislikes: 0
# Total Accepted:    64.5K
# Total Submissions: 89.1K
# Testcase Example:  '["bella","label","roller"]'
#
# 给你一个字符串数组 words ，请你找出所有在 words 的每个字符串中都出现的共用字符（ 包括重复字符），并以数组形式返回。你可以按 任意顺序
# 返回答案。
# 
# 
# 示例 1：
# 
# 
# 输入：words = ["bella","label","roller"]
# 输出：["e","l","l"]
# 
# 
# 示例 2：
# 
# 
# 输入：words = ["cool","lock","cook"]
# 输出：["c","o"]
# 
# 
# 
# 
# 提示：
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 100
# words[i] 由小写英文字母组成
# 
# 
#

# @lc code=start
class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        from collections import Counter
        
        d = Counter(words[0])
        for word in words[1:]:
            d = d & Counter(word)
        ll = [[item] * times for item, times in d.items()]
        return sum(ll, [])
# @lc code=end

