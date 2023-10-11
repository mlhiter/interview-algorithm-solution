# https://leetcode.cn/problems/remove-duplicates-from-sorted-list/description/
# 难度：simple


# 解法一:一次遍历
# 思路:由于链表已排好序,因此重复元素在链表中出现的位置是连续的,因此一次遍历即可删除重复元素
# 复杂度:时间复杂度O(n),空间复杂度O(1)

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head

        cur = head
        while cur.next:
            if cur.val == cur.next.val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return head
