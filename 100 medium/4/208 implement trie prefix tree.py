""" https://leetcode.com/problems/implement-trie-prefix-tree/
Implement a trie with insert, search, and startsWith methods.

Example:

Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // returns true
trie.search("app");     // returns false
trie.startsWith("app"); // returns true
trie.insert("app");
trie.search("app");     // returns true
Note:

You may assume that all inputs are consist of lowercase letters a-z.
All inputs are guaranteed to be non-empty strings.


['hello' , 'hey']

                h
               /
              e
             /  \
            l     y
           /      \
          l        *
         /
        l
       /
     o
    /
   *

"""


class TrieNode:
    def __init__(self):
        self.is_word_end = False
        self.childNodes = {}


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        cur = self.root
        for c in word:
            if c not in cur.childNodes:
                cur.childNodes[c]=TrieNode()
            cur = cur.childNodes[c] # move cur to the next level
        cur.is_word_end = True # mark this path as a string word

    def startsWith(self, prefix):
        cur = self.root
        for c in prefix:
            if c not in cur.childNodes:
                return False
            cur = cur.childNodes[c]
        return True

    def search(self, word):
        cur = self.root
        for c in word:
            if c not in cur.childNodes:
                return False
            cur = cur.childNodes[c]
        return cur.is_word_end

# Your Trie object will be instantiated and called as such:
if __name__ == '__main__':
    word = 'ten'
    obj = Trie()
    obj.insert(word)
    param_2 = obj.search(word)
    # param_3 = obj.startsWith(prefix)
