"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

class Sol:

    def isv(self, s):
        stack = []
        for c in s:
            if c in ('(', '[', '}'):
                stack.append(c)
            elif c in (')', ']', '}'):
                if not stack:
                    return False
                prev = stack.pop()
                if (c == ')' and prev != '(') or (c == ']' and prev !='[') or (c == '}' and prev !='{'):
                    return False
        return True if not stack else False







