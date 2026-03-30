class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = list()
        for i in tokens:
            if i not in ["+", "-", "*", "/"]:
                stack.append(int(i))


            elif i == "+":
                stack.append(stack.pop() + stack.pop())

            elif i == "-":
                diff_1 = stack.pop()
                diff_2 = stack.pop()
                stack.append(diff_2 - diff_1)

            elif i == "*":
                stack.append(stack.pop() * stack.pop())

            elif i == "/":
                div1 = stack.pop()
                div2 = stack.pop()
                stack.append(int(div2/div1))

        return int(stack.pop())
            