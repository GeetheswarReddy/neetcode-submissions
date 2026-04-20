class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        valid=["+","-","*","/"]
        for i in tokens:
            if i in valid:
                b=int(stack.pop())
                a=int(stack.pop())
                match i:
                    case '+':
                        stack.append(a+b)
                    case '-':
                        stack.append(a-b)
                    case '*':
                        stack.append(a*b)
                    case '/':
                        stack.append(a/b)
            else:
                stack.append(i)
        return int(stack.pop())