""" https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
Given a n x n matrix where each of the rows and columns are sorted in ascending order,
find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order, not the kth distinct element.

Example:

matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
],
k = 8,

return 13.
Note:
You may assume k is always valid, 1 ≤ k ≤ n2.


找到第k小个数。

Heap data structure is mainly used to represent a priority queue. In Python, it is available using “heapq” module.
 The property of this data structure in Python is that each time the smallest of heap element is popped(min heap).
"""
class Solution:
    def kthSmallest(self, matrix, k):
        temp =[]

        for i in matrix:
            temp += i
        temp = sorted(temp)

        return temp[k -1]
    def kthSmallest(self, matrix, k):
        import heapq
        q = []
        heapq.heapify(q)

        row = len(matrix)
        col = len(matrix[0])

        for i in range(row):
            for j in range(col):
                heapq.heappush(q, matrix[i][j])
        for j in range(k):
            res = heapq.heappop(q)
        return res