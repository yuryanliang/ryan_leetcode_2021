""" https://leetcode.com/problems/spiral-matrix-ii/
Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.

Example:

Input: 3
Output:
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""
class Solution:
    def generateMatrix(self, n):
        matrix = [[0 for _ in range(n)] for _ in range(n)]

        left = 0
        right = n -1
        top = 0
        bottom = n-1

        val = 1
        while left <= right and top <= bottom:
            for i in range(left, right + 1):
                matrix[top][i] = val
                val +=1
            for j in range(top + 1, bottom):
                matrix[j][right] = val
                val +=1

            for i in reversed(range(left, right + 1)):
                if left < right:
                    matrix[bottom][i] = val
                    val += 1
            for j in reversed(range(top + 1, bottom)):
                if top < bottom:
                    matrix[j][left] = val
                    val +=1

            left +=1
            right -=1
            top +=1
            bottom -= 1
        return matrix

if __name__ == '__main__':
    print(Solution().generateMatrix(3))