"""https://leetcode.com/problems/interleaving-string/
Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
Note: a + b is the concatenation of strings a and b.



Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
Example 3:

Input: s1 = "", s2 = "", s3 = ""
Output: true


Constraints:

0 <= s1.length, s2.length <= 100
0 <= s3.length <= 200
s1, s2, and s3 consist of lowercase English letters.


Follow up: Could you solve it using only O(s2.length) additional memory space?
"""
class Solution:
    def IsInterleave(self, s1, s2, s3):
        m, n, l = len(s1), len(s2), len(s3)
        if m+n != l:
            return False
        dp = [[True for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, n +1):
            dp[0][j] = dp[0][j-1] and s2[j -1] == s3[j-1]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j]= (dp[i-1][j] and s1[i -1] == s3[i -1 + j]) or (dp[i][j -1] and s2[j -1]==s3[i + j -1])
        return dp[-1][-1]
if __name__ == '__main__':
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(Solution().IsInterleave(s1,s2,s3))