class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count_s, count_t = {}, {}
        for si in s:
            count_s[si] = count_s.get(si, 0) + 1
        for ti in t:
            count_t[ti] = count_t.get(ti, 0) + 1

        if count_s==count_t:
            return True
        else:
            return False