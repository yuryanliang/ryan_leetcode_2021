""" https://leetcode.com/problems/word-break/
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
"""
"""
https://www.cnblogs.com/grandyang/p/4257740.html
这道题其实还是一道经典的 DP 题目，也就是动态规划 Dynamic Programming。博主曾经说玩子数组或者子字符串且求极值的题，基本就是 DP 没差了，虽然这道题没有求极值，但是玩子字符串也符合 DP 的状态转移的特点。
DP 解法的两大难点，定义 dp 数组跟找出状态转移方程，先来看 dp 数组的定义，这里我们就用一个一维的 dp 数组，其中 dp[i] 表示范围 [0, i) 内的子串是否可以拆分，注意这里 dp 数组的长度比s串的长度大1，
是因为我们要 handle 空串的情况，我们初始化 dp[0] 为 true，然后开始遍历。
注意这里我们需要两个 for 循环来遍历，因为此时已经没有递归函数了，所以我们必须要遍历所有的子串，我们用j把 [0, i)
 范围内的子串分为了两部分，[0, j) 和 [j, i)，其中范围 [0, j) 就是 dp[j]，范围 [j, i) 就是 s.substr(j, i-j)，其中 dp[j] 是之前的状态，我们已经算出来了
 ，可以直接取，只需要在字典中查找 s.substr(j, i-j) 是否存在了，如果二者均为 true，将 dp[i] 赋为 true，并且 break 掉，此时就不需要再用j去分 [0, i) 范围了，因为 [0, i) 范围已经可以拆分了。
 最终我们返回 dp 数组的最后一个值，就是整个数组是否可以拆分的布尔值了，代码如下
玩子数组或者子字符串且求极值的题，基本就是 DP 没差了
其中 dp[i] 表示范围 [0, i) 内的子串是否可以拆分，注意这里 dp 数组的长度比s串的长度大1，是因为我们要 handle 空串的情况，我们初始化 dp[0] 为 true，
Dp:
从0开始，若此分隔存在于给定字典中，则可以断开。

s = "leetcode", wordDict = ["leet", "code"]

leetcode
  l e e t c o d e 
T F F F F F F F F 

leet
s[0:0+4] in wordDict

s[0+4] = True

  l e e t c o d e 
T F F F T F F F F 
        当搜索到这里时会再次进行重复的搜索。
"""


class Solution:
    def wordBreak(self, s, wordDict):
        dp = [False] * (len(s) + 1) # dp[i] means s [:i + 1] can be segmented into words in the wordDicts
        dp[0] = True # 注意这里 dp 数组的长度比s串的长度大1，是因为我们要 handle 空串的情况，我们初始化 dp[0] 为 true，
        for i in range(len(s)):
            for j in range(i, len(s)):
                temp = s[i: j + 1]
                if dp[i] and temp in wordDict:
                    dp[j + 1] = True
        return dp[-1]

    def test(self,s): # 第一位穷举， 前两位穷举， 前三位穷举
        for i in range(len(s)):
            for j in range(i + 1):
                print(s[j: i+1])
            # a
            # ab
            # b
            # abc
            # bc
            # c

    def test_1(self,s): # 第一个开头 穷举， 第二个开头 穷举， 第三个开头穷举
        for i in range(len(s)):
            for j in range(i + 1, len(s)+1):
                print(s[i: j])
            # a
            # ab
            # abc
            # b
            # bc
            # c

if __name__ == "__main__":
    # Solution().test_1("abc")
    # print (Solution().wordBreak("goalspecial", ["go", "goal", "goals", "special"]))
    print (Solution().wordBreak("leetcode", ["leet", "code"]))
    # print (Solution().wordBreak("aaaaa", ["aaa", "aa"]))