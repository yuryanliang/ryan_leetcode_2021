""" https://leetcode.com/problems/permutations/
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
"""

"""
backtracking

因为没有重复的数， 所以在加入alist 之前可以判断一下是不是 这个数已经取过。
"""
class Sol:
    def permute(self, nums):
        res = []
        path = [] #代表已取出的数
        self.helper(nums, path, res)
        return res
    def helper(self, nums, path, res):
        if len(path) == len(nums):
            temp = path.copy()
            res.append(temp)
            return
        for i, item in enumerate(nums):
            if item not in path: #取过的数不再取
                path.append(item)
                self.helper(nums, path, res)
                 #重要！！遍历过此节点后，
                # 要回溯到上一步，因此要把加入到结果中的此点去除掉！
                path.pop()