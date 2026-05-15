class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        found = []
        for n in nums:
            if n in found: return True
            found.append(n)
        return False