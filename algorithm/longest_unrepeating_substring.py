# LeetCode LCR 016. 无重复字符的最长子串
# 滑动窗口

from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """ 计算子串的长度 """
        res = deque()
        res_len = 0
        right = 0
        while right < len(s):
            # 如果当前滑动窗口中没有当前元素，那么添加上
            if s[right] not in res:
                res.append(s[right])
                right += 1
            # 如果当前滑动窗口中有当前元素，那么不要添加当前元素，而是弹出窗口最左边的元素
            else:
                res.popleft()
            # 比较这一轮的子串长度和此前最长的子串长度
            res_len = max(res_len, len(res))
        return res_len
    
    def longestSubstring(self, s: str) -> int:
        """ 输出最长的子串 """
        res = deque()
        ans = []
        right = 0
        while right < len(s):
            if s[right] not in res:
                res.append(s[right])
                right += 1
            else:
                res.popleft()
            # 如果 已保存的子串长度 < 这一轮的子串长度，那么更新子串
            if len(ans) < len(res):
                ans = res.copy()
        return ans

s = "abcabcbb"
mysolution = Solution()
print(mysolution.lengthOfLongestSubstring(s))
print(mysolution.longestSubstring(s))