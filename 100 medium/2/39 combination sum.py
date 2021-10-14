""" https://leetcode.com/problems/combination-sum/
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]
Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
"""
"""
backtracking
初始 res， 也许start， path

进入helper， 先判断什么时候加结果， len（path）= len（nums） 或者直接就加， 要考虑dedup 要copy temp

然后for loop，从start或者i开始， 先加入path。 然后call helper， 然后pop
"""
class Sol:
    def comb_sum(self, candidates, target):
        if not candidates:
            return []

        result = []
        path = []  # numbers that already used

        start = 0 # need to use a start point otherwise it exceed time limit

        self.helper(candidates, start, path, target, result)
        return result
    def helper(self, cand, start, path, target, res):
        if sum(path) == target:
            temp= path.copy()
            temp.sort()
            if temp not in res:
                res.append(temp)

        while start < len(cand) and sum(path)< target:
            path.append(cand[start])
            self.helper(cand, start, path, target, res)
            path.pop()
            start +=1