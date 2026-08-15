class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = { ")" : "(", "]" : "[", "}" : "{" }

        # check for each char in the string
        for c in s:
            if c in pairs:
                # check if stack is not empty and last position of stack is equals to pairs, then pop
                if stack and stack[-1] == pairs[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        # return true if stack is empty else false
        return True if not stack else False