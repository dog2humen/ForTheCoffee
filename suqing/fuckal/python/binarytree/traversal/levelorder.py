# coding:utf8

def level_order(root):
    res = []
    if not root:
        return res
    level = [root]
    while level:
        cur, new_level = [], []
        for node in level:
            cur.append(node.val)
            if node.left:
                new_level.append(node.left)
            if node.right:
                new_level.append(node.right)

        level = new_level
        res.append(cur)

    return res


