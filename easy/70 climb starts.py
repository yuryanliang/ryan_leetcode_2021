"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""


class Sol:
    # brute force/ recursion
    def brute_force(self, n):
        if n == 1 or n == 0:
            return 1
        else:
            return self.brute_force(n - 1) + self.brute_force(n - 2)
    # two function
    def two_function(self, n):
        return self.climb(n)
    def climb(self, n):
        if n == 0 or n == 1:
            return 1
        else:
            return self.climb(n -1 )+ self.climb(n -2)

    # two function with memo
    def two_function_memo(self, n):
        dp = [-1 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 1
        return self.climb_memo(n, dp)
    def climb_memo(self, n , dp):
        for i in range(2, n + 1):
            dp[i] = dp[i -1 ] + dp[i -2]
        return dp[n]

    # one function + memo -> dp
    # time complexity will be O(n) and our space will also be O(n), since we create a 1D array from 0 to n.
    def one_func_dp(self, n):
        dp = [1 for _ in range(n + 1)]
        for i in range(2, n + 1):
            dp[i] = dp[i -1] + dp[i -2]
        return dp[n]
