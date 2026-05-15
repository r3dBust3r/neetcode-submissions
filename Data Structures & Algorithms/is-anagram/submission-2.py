class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = dict()
        for n in s:
            if n not in s_count: s_count[n] = 0
            else: s_count[n] += 1

        t_count = dict()
        for n in t:
            if n not in t_count: t_count[n] = 0
            else: t_count[n] += 1

        if len(s_count) != len(t_count): return False
        for k, v in s_count.items():
            if k not in t_count: return False
            if v != t_count[k]: return False
        return True

