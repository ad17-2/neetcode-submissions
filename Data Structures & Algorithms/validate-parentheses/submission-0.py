class Solution:
    def isValid(self, s: str) -> bool:

        tmp = {")": "(", "]": "[", "}": "{"}

        stack = []

        for c in s:
            if c not in tmp:
                stack.append(c)
                continue
            if not stack or stack[-1] != tmp[c]:
                return False
            stack.pop()

        return not stack
        