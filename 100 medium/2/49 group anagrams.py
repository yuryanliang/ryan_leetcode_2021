""" https://leetcode.com/problems/group-anagrams/
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""

"""
把每一个sort 过的str 做成key， 把str 做成value

用try except 做append 或者附上新值
"""

class Sol:
    def group(self, strs):
        res = {}

        for i in strs:
            key = ''.join(sorted(i))

            try:
                res[key].append(i)
            except:
                res[key] = i
        return res.values()