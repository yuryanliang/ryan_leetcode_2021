""" https://leetcode.com/problems/decode-ways/
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""

"""
dp问题 ， 有多少种方法破解。 

one step: dp[i]= dp[i - 1] if i-1位 不是0
two step: dp[i] = dep[i -2] if i-2和i-1 在10到26之间

 dp[1] = 0 if s[0] == "0" else 1
# https://leetcode.com/problems/decode-ways/discuss/253018/Python%3A-Easy-to-understand-explanation-bottom-up-dynamic-programming

"""
class Solution:
    def numDecodings(self, s):
        if not s:
            return 0
        dp = [0 for _ in range(len(s) + 1)] # dp[i] is the ways to parse s[1 : i + 1]

        dp[0] = 1
        dp[1] =0 if s[0] == "0" else 1

        for i in range(2, len(s) + 1):
            # one-step jump
            pre_one = int(s[i -1: i])
            if 0<pre_one <=9:  # not equal to 0
                dp[i]+=dp[i-1]
            # two-step jump
            pre_two = int(s[i-2: i])
            if 10<= pre_two <=26:  # from 10 to 26
                dp[i] += dp[i-2]
        return dp[len(s)]

if __name__ == "__main__":
    print(Solution().numDecodings("236"))
    for i in ["0", "10", "103", "1032", "10323"]:
        print(Solution().numDecodings(i))
