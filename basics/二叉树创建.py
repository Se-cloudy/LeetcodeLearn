class TreeNode():
    def __init__(self, val, lchild=None, rchild=None):
        self.val = val
        self.lchild = lchild
        self.rchild = rchild


def create_tree(root, vals):
    while (len(vals != 0)):
        if vals[0] == '#':
            vals.pop()
            root = None
            return root
        else:
            root = TreeNode(vals[0])
            vals.pop()
            root.lchild = create_tree(root.lchild, vals)
            root.rchild = create_tree(root.rchild, vals)
            return root


if __name__ == '__main__':
    root = None
    vls = 'abc##d##e##'  # 前序遍历扩展的二叉树序列
    vls = list(vls)
    roots = create_tree(root, vls)
    print(roots)
