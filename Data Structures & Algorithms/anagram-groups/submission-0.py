class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs: return []

        new_lst = {}
        for s in strs:
            key_s = ''.join(sorted(s))
            if key_s not in new_lst:
                new_lst[key_s] = []
            new_lst[key_s].append(s)

        return [new_lst[lst] for lst in new_lst]