# https://leetcode.com/problems/evaluate-reverse-polish-notation/

# Evaluate the value of an arithmetic expression in Reverse Polish Notation.

# Valid operators are +, -, *, and /. Each operand may be an integer or another
# expression.

# Note that division between two integers should truncate toward zero.

# It is guaranteed that the given RPN expression is always valid. That means the
# expression would always evaluate to a result, and there will not be any division
# by zero operation.

################################################################################

# use stack and pop nums when encounter operators

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for t in tokens:
            if t not in "+-*/":
                stack.append(int(t))
            else:
                num2 = stack.pop()
                num1 = stack.pop()
                if t == "+":
                    stack.append(num1 + num2)
                elif t == "-":
                    stack.append(num1 - num2)
                elif t == "*":
                    stack.append(num1 * num2)
                elif t == "/":
                    stack.append(int(num1 / num2))
        return stack.pop()
