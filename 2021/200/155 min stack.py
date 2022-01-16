""" https://leetcode.com/problems/min-stack/
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.


Evalample 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Evalplanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2


Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin
"""
class MinStack:
    def __init__(self):
        self.q = []
    def push(self, val):
        curMin = self.getMin()
        if curMin == None or val < curMin:
            curMin = val
        self.q.append((val, curMin))

    def pop(self):
        self.q.pop()

    def top(self):
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]
    def getMin(self):
        return self.q[len(self.q)-1][1]
