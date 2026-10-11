class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        solutions=[]
        def isvalid(paranthesis):
            stack=[]
            for i in paranthesis:
                if i=="(":
                    stack.append("(")
                else:
                    if len(stack)==0:
                        return False
                    stack.pop()
            if len(stack)==0:
                return True
        def backtrack(curr):
            if len(curr)==n*2:
                if isvalid(curr):
                    solutions.append(curr)
                return
            backtrack(curr+")")
            backtrack(curr+"(")

        backtrack("")
        return solutions
        