class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        l = len(nums)
        for i in range(l):
            r = 1
            for j in range(l):
                if i == j: continue
                r = r * nums[j]
            res.append(r)
        return res
