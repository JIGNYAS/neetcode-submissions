class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closehash = {")": "(", "}": "{", "]": "["}

        for i in s:
            if i in closehash:
                if stack and stack[-1] == closehash[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False
