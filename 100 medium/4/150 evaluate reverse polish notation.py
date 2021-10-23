"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:

Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a result and there won't be any divide by zero operation.
Example 1:

Input: ["2", "1", "+", "3", "*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: ["4", "13", "5", "/", "+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
Output: 22
Explanation:
  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22

"""

"""
 1. 使用栈的原因：每个操作符需要使用最近的两个数
 2. 需要分清左右数
 3. 需要注意读的是字符
 4. python的除法int(a / b)代替其他语言的a / b, a // b 并不是直接扔掉非0部分(在负数部分，比如-1.8333会变成-2，而在其他语言里是-1)
    如果硬要用，就需要讨论是否为负数而且是否能除尽的问题：(a // b) + 1 if a // b < 0 and a % b != 0 else a // b
 """
class Solution:
    def evalRPN(self, tokens):
        stack =[]
        for token in tokens:
            if token in ['+', '-', '*', '/']:
                b, a = stack.pop(), stack.pop()
                if token == '+':
                    res = a + b
                if token == '-':
                    res = a - b
                if token == '*':
                    res = a * b
                if token == '/':
                    res = int(float(a)/float(b))
                stack.append(res)
            else:
                stack.append(int(token))
        return stack.pop()

if __name__ == "__main__":
    a = 3
    b= -2
    res = int(float(a) / float(b))
    r = a/b
    u = a//b
    1==1
    # print(Solution().evalRPN(["2", "1", "+", "3", "*"]))
    # print (Solution().evalRPN(["4", "13", "5", "/", "+"]))
    # print (Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))