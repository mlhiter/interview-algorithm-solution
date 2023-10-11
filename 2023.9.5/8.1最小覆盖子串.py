# https://leetcode.cn/problems/minimum-window-substring/description/
# 难度：hard


# 解法一：滑动窗口
# 思路：用两个指针i，j表示滑动窗口的左右边界。
# 复杂度：时间复杂度O(n),空间复杂度O(k),k为S和T中的字符集合

"""
步骤：1，不断增加j使滑动窗口增大，直到包含T的所有元素
    2，不断增加i使窗口缩小，直到遇到一个必须包含的元素，记录当前窗口长度
    3，i增加一个位置，此时窗口不满足条件，则转向步骤一，寻找新的窗口，直到j超过字符串范围
"""


from typing import Collection


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Collection.defaultdict(int)  # 记录每个字符的需要量的字典
        for c in t:
            need[c] += 1
        needCnt = len(t)  # 记录t中字符需要量
        i = 0
        res = (0, float("inf"))  # 窗口数组
        for j, c in enumerate(s):  # 同时获取数组值c和索引j
            if need[c] > 0:  # 只有t中字符需要量才会大于0，这里是t中字符
                needCnt -= 1
            need[c] -= 1
            if needCnt == 0:  # 此时包含所有的T元素
                while True:  # 增加i使窗口缩小
                    c = s[i]
                    if need[c] == 0:  # 当碰到t中字符则停止
                        break
                    need[c] += 1
                    i += 1
                if j - i < res[1] - res[0]:  # 如果窗口缩小则更新窗口
                    res = (i, j)
                need[s[i]] += 1  # i右移，相应need值增加
                needCnt += 1
                i += 1
        # 裁切数组
        return "" if res[1] > len(s) else s[res[0] : res[1] + 1]
