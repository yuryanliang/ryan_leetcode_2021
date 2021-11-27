""" https://leetcode.com/problems/multiply-strings/
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.



Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"


Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
"""
class Solution:
    def multiply(self, num1, num2):
        num1 = num1[::-1]
        num2 = num2[::-1]

        res = [0]*(len(num1) + len(num2))

        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += int(num1[i]) * int(num2[j])
                res[i + j + 1] +=(res[i + j ] //10)
                res[i + j] %=  10
        #trim leading 0
        i = len(res)-1
        while i >0 and res[i] == 0:
            i -=1
        return ''.join(map(str, res[i::-1]))
if __name__ == '__main__':
    num1 = "123"
    num2 = "456"
    print(Solution().multiply(num1,num2))