""" https://leetcode.com/problems/bulls-and-cows/
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.

Example 1:

Input: secret = "1807", guess = "7810"

Output: "1A3B"

Explanation: 1 bull and 3 cows. The bull is 8, the cows are 0, 1 and 7.
Example 2:

Input: secret = "1123", guess = "0111"

Output: "1A1B"

Explanation: The 1st 1 in friend's guess is a bull, the 2nd or 3rd 1 is a cow.
Note: You may assume that the secret number and your friend's guess only contain digits, and their lengths are always equal.
"""
class Solution:
    def getHint(self, secret, guess):
        bull, cow = 0, 0
        lookup = {}

        for i, val in enumerate(secret):
            if val == guess[i]:
                bull += 1
            else:
                lookup[val]= lookup.get(guess[i],0) + 1 # Optional. A value to return if the specified key does not exist.

        # lookup : {'1':1, '0':2, '7':3}

        for i, val in enumerate(secret):
            if val != guess[i] and lookup.get(guess[i], 0) !=0:
                cow +=1
                lookup[guess[i]] -=1
        return str(bull) + 'A' + str(cow) + 'B'

    def getHint1(self, secret, guess):
        secret_map, guess_map = {}, {}
        bull, cow = 0, 0

        for i, val in enumerate(secret):
            if val == guess[i]:
                bull += 1
            else:
                if val in secret_map:
                    secret_map[val] += 1
                else:
                    secret_map[val] = 1
                if guess[i] in guess_map:
                    guess_map[guess[i]] +=1
                else:
                    guess_map[guess[i]]= 1

# guess_map {'7': 1, '1': 1, '0': 1}
# secret_map{'1': 1, '0': 1, '7': 1}

        for i in guess_map:
            if i in secret_map:
                cow += min(secret_map[i], guess_map[i])
        return str(bull) + 'A' + str(cow) + 'B'

if __name__ == '__main__':
    secret = "1807"
    guess = "7810"
    # secret = "1123"
    # guess = "0111"
    print(Solution().getHint(secret, guess))