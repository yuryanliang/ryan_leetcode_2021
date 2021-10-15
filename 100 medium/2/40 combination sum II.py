""" https://leetcode.com/problems/combination-sum-ii/
Given a collection of candidate numbers (candidates) and a target number (target),
find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

All numbers (including target) will be positive integers.
The solution set must not contain duplicate combinations.
Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""
class Sol:
    def comb(self, candidates, target):
        candidates.sort()
        res = []
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if sum(path) > target:
            return
        if target == sum(path):
            if path not in res:
                res.append(path)
            return
        for i in range(index, len(nums)):
            self.dfs(nums, target, i + 1, path + [nums[i]], res)


def main():
    candidates= [10,1,2,7,6,1,5]
    target = 8
    # candidates= [1,2]
    # target = 4
    print(Sol().comb(candidates,target))


if __name__ == '__main__':
    main()
