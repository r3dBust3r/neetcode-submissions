class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) == 1:
            if nums[0] == target: return 0
            return -1

        old_nums = nums[:]
        while 1:
            center = len(nums) // 2
            if nums[center] == target:
                return old_nums.index(target)

            elif nums[center] < target:
                nums = nums[center:]

            elif nums[center] > target:
                nums = nums[:center]

            if len(nums) == 1 and nums[0] != target:
                return -1
