class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1_sorted = sorted(s)
        t1_sorted = sorted(t)

        s_len = len(s)
        t_len = len(t)

        if s_len != t_len:
            return False

        return s1_sorted == t1_sorted

