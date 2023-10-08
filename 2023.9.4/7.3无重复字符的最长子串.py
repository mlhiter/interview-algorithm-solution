# https://leetcode.cn/problems/longest-substring-without-repeating-characters/
# 难度:medium


# 解法一：滑动窗口（不定长度）
# 思路：维护一个不重复元素的窗口，当新元素与其中元素重复时则删除旧的重复元素及其左侧的元素，并且更新最大长度
# 复杂度：时间复杂度O(n),空间复杂度O(s)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        left = 0
        lookup = set()  # 当前窗口集合
        n = len(s)
        max_len, cur_len = 0, 0  # 最大长度和当前长度
        for i in range(n):
            cur_len += 1

            # 窗口内容删除
            while s[i] in lookup:  # 当出现重复数字时删除重复数字及其左侧的元素
                lookup.remove(s[left])
                left += 1
                cur_len -= 1

            # 当前长度用来更新最大长度
            if cur_len > max_len:
                max_len = cur_len

            # 如果不和窗口内元素重复则加入窗口
            lookup.add(s[i])
        return max_len
