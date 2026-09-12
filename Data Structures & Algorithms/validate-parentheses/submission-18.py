class Solution:
    def isValid(self, s: str) -> bool:



        stack = []

        open_brackets = {"(", "[", "{"}
        closed_brackets = {")", "]", "}"}


        for bracket in s:

            if len(stack) == 0 and bracket in closed_brackets:
                return False

            elif bracket in open_brackets:
                stack.append(bracket)
            
            else:
                closed_bracket = bracket

                if stack[-1] == "(" and closed_bracket != ")":
                    return False
                elif stack[-1] == "[" and closed_bracket != "]":
                    return False
                elif stack[-1] == "{" and closed_bracket != "}":
                    return False
                else:
                    stack.pop()
        
        if len(stack) != 0:
            return False
            
        return True

