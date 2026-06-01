
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l = len(temp)
        res = []
        for i in range(l):
            c = 0
            found = False
            for j in range(i + 1, l):
                c += 1
                if temp[j] > temp[i]:
                    found = True
                    break

            res.append(c) if found else res.append(0)

        return res
