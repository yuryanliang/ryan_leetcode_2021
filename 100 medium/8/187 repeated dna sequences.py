""" https://leetcode.com/problems/repeated-dna-sequences/
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T, for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule.

Example:

Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"

Output: ["AAAAACCCCC", "CCCCCAAAAA"]
"""


class Solution:
    def dna(self, s):
        lookup = {}
        res = []
        for i in range(len(s) - 9):
            sub = s[i: i + 10]
            if sub in lookup:
                lookup[sub] += 1
                if lookup[sub] == 2:
                    res.append(sub)
            else:
                lookup[sub] = 1
        return res


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print(Solution().dna(s))
