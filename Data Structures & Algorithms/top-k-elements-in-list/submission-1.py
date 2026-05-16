class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for n in nums:
            if n not in counter: counter[n] = 1
            else: counter[n] += 1
        return sorted(counter, key=counter.get)[-k:]
