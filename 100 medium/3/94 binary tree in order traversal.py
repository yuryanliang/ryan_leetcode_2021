"""

Given a binary tree, return the inorder traversal of its nodes' values.

For example:
Given binary tree [1,null,2,3],
   1
    \
     2
    /
   3
return [1,3,2].



"""
"""
使用辅助结点p， 相当于cur指针
如果存在p， 则一直 把 left 压入 stack中， 并且p向left结点移动， 所以stack是按照，左 中， 左， 中的顺序压入。
如果没有p， 从 stack 中取出值 left，（相当于inorder(root.left))  放入结果 ( 相当于print root）， 然后p指向right（相当于inorder(root.right))


""""""
根据中序遍历的顺序，对于任一结点，优先访问其左孩子，而左孩子结点又可以看做一根结点，然后继续访问其左孩子结点，直到遇到左孩子结点为空的结点才进行访问，然后按相同的规则访问其右子树。因此其处理过程如下：

对于任一结点P，

(1)若其左孩子不为空，则将P入栈并将P的左孩子置为当前的P，然后对当前结点P再进行相同的处理；

(2)若其左孩子为空，则取栈顶元素并进行出栈操作，访问该栈顶结点，然后将当前的P置为栈顶结点的右孩子；

(3)直到P为NULL并且栈为空则遍历结束s

https://www.geeksforgeeks.org/tree-traversals-inorder-preorder-and-postorder/
"""

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self, root):
        res =[]
        stack =[]
        todo = root # like cur pointer

        while stack or todo:
            if todo:
                stack.append(todo)
                todo = todo.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                todo =temp.right
        return res


if __name__ == "__main__":
    root = TreeNode(1)
    # root.left = TreeNode(9)
    root.right = TreeNode(2)
    root.right.left = TreeNode(3)
    # root.right.right = TreeNode(7)
    result = Solution().inorderTraversal(root)
    print (result)

# iteration
class Traversal:
    def pre_order_template(self, root):
        res =[]
        stack = []
        p = root

        if p or stack:
            if p:
                stack.append(p)
                res.append(p.val)
                p = p.left
            else:
                temp = stack.pop()
                p= temp.right
        return res
    def in_oder_template(self, root):
        res = []
        stack =[]
        p = root

        if p or stack:
            if p:
                stack.append(p)
                p = p.left
            else:
                temp = stack.pop()
                res.append(temp.val)
                p = temp.right
        return res
    def post_order_template(self, root):
        res = []
        stack =[]
        p = root

        if p or stack:
            if p:
                stack.append(p)
                res.insert(0, p.val)
                p= p.right
            else:
                temp = stack.pop()
                p = temp.left
        return res


class Sol:
    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        return res
    def helper(self, root, res):
        if not root:
            return
        if root.left:
            self.helper(root.left, res)
        res.append(root.val)
        if root.right:
            self.helper(root.right, res)

class Recursion:
    def pre_order(self, node):
        if not node:
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)
    def in_oder(self, node):
        if not node:
            return
        self.in_oder(node.left)
        print(node.val)
        self.in_oder(node.right)
    def post_order(self, node):
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)