""" https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
Find the length of the longest substring T of a given string (consists of lowercase letters only) such that every character in T appears no less than k times.

Example 1:

Input:
s = "aaabb", k = 3

Output:
3

The longest substring is "aaa", as 'a' is repeated 3 times.
Example 2:

Input:
s = "ababbc", k = 2

Output:
5

The longest substring is "ababb", as 'a' is repeated 2 times and 'b' is repeated 3 times.
"""
class Solution:
    def longestSubstring(self, s ,k):
        from collections import Counter
        counter = Counter(s)

        for char, ct in counter.items():
            if ct <k:
                return max(self.longestSubstring(sub_string, k) for sub_string in s.split(char))

        return len(s)

if __name__ == '__main__':
    s = "aebabbc"
    k = 2
    print(Solution().longestSubstring(s, k))