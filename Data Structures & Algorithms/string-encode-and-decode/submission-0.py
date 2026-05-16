class Solution:
    from random import randint
    space = '%20'
    key   = randint(1, 9)

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            encoded_s = ''
            for c in s:
                encoded_s += chr(ord(c) + Solution.key)
            res += encoded_s + Solution.space
        suffx = '=' * (len(res) % 5)
        return res + suffx


    def decode(self, s: str) -> List[str]:
        strs = s.split(Solution.space)
        res = []
        for s in strs:
            res.append(''.join([chr(ord(c) - Solution.key) for c in s]))
        return res[:-1]