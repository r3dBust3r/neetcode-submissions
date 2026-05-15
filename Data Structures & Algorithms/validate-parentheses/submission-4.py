class Solution:
    def isValid(self, s: str) -> bool:
        opened = ""
        for c in s:
            if c in ['(', '[', '{']:
                opened += c
                continue

            if c in [')', ']', '}'] and not len(opened):
                return False

            if c == ')':
                if opened[-1] != '(':
                    return False
                opened = opened[:-1]

            if c == ']':
                if opened[-1] != '[':
                    return False
                opened = opened[:-1]

            if c == '}':
                if opened[-1] != '{':
                    return False
                opened = opened[:-1]
                
        return True if not len(opened) else False
                