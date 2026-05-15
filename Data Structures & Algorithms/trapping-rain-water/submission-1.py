class Solution:
    def trap(self, height: List[int]) -> int:
        count = 0
        for i in range(len(height)):
            if i == 0 or i == len(height) - 1: continue
            current = min(max(height[:i]), max(height[i:])) - height[i]
            count += current if current > 0 else 0
        return count