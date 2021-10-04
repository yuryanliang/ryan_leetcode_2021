""" https://leetcode.com/problems/add-binary/
Given two binary strings a and b, return their sum as a binary string.



Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"


Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

# The idea is similar to https://leetcode.com/problems/add-two-numbers/
# -- iterate backwards and build the result from the back by adding two last digits while keeping carry in mind.
# In the end, if carry is non-zero we append it to the front.

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        result = ""
        i, j = len(a) - 1, len(b) - 1
        while i >= 0 or j >= 0:
            a_digit = int(a[i]) if i >= 0 else 0
            b_digit = int(b[j]) if j >= 0 else 0
            _sum = a_digit + b_digit + carry
            digit = _sum % 2
            carry = _sum // 2
            result = str(digit) + result
            i -= 1
            j -= 1
        if carry:
            result = str(carry) + result
        return result

        # add two binary from back to front, I think it is very self explained, when 1+1 we need a carry.
        # The time complex is O(m+n+c)，it's linear, where m=len(a)，n=len(b) and c="count of carries, which is less than min(m,n)".

    class Solution:
        def addBinary(self, a, b):
            if len(a) == 0: return b
            if len(b) == 0: return a
            if a[-1] == '1' and b[-1] == '1':
                return self.addBinary(self.addBinary(a[0:-1], b[0:-1]), '1') + '0'
            if a[-1] == '0' and b[-1] == '0':
                return self.addBinary(a[0:-1], b[0:-1]) + '0'
            else:
                return self.addBinary(a[0:-1], b[0:-1]) + '1'