class Solution:
    def trap(self, height: List[int]) -> int:
        h = len(height)
        count = 0
        for i in range(h):
            if i in [0, h-1]: continue
            current = min(max(height[:i]), max(height[i:])) - height[i]
            count += current if current > 0 else 0
        return count