class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums: return 0

        nums = sorted(set(nums))
        count = {}

        l = len(nums)
        for i in range(l):
            c = 1
            k = 1
            for j in range(i + 1, l):
                if nums[i] + k == nums[j]:
                    c += 1
                k += 1

            count[nums[i]] = c

        return max([c for c in count.values()])

