class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        left = 0
        tmp = set()

        n = len(s)

        for i in range(n):
            while s[i] in tmp:
                tmp.remove(s[left])
                left+=1
            tmp.add(s[i])
            res = max(res, i - left + 1)
        return res