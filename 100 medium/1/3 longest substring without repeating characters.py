""" https://leetcode.com/problems/longest-substring-without-repeating-characters/
Given a string s, find the length of the longest substring without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
Example 4:

Input: s = ""
Output: 0


Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

class Sol:
    def sol1(self,s):
        res = 0
        for i in range(len(s)):
            j = i + 1
            lookup = {s[i] : i}
            while j < len(s):
                if s[j] in lookup:
                    res = max(res, j - i )
                    break
                else:
                    lookup[s[j]] = j

                j+=1
            if j == len(s): # when s = 'au' , edge case
                res = max(res, j - i)
        return res

    def sol2(self, s):
        used = {}
        res = start = 0
        for i, c in enumerate(s):
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                res = max(res,  i - start + 1)
            used[c] = i

        return res