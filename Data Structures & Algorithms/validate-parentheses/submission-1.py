class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        tmp = { ")" : "(", "]" : "[", "}" : "{" }

        for item in s:
            if item not in tmp:
                stack.append(item)
            else:
                if stack and stack[-1] == tmp[item]:
                    stack.pop()
                else:
                    return False

        if not stack:
            return True
        else:
            return False