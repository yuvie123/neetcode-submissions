class Solution:
    def isValid(self, s: str) -> bool:

        # Fastest way to code solution

        stack = []
        closedAndOpen = {")" : "(", "]" : "[", "}" : "{"}

        for bracket in s:
            if bracket in closedAndOpen:
                if stack and stack[-1] == closedAndOpen[bracket]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(bracket)

        if stack:
            return False
        else:
            return True