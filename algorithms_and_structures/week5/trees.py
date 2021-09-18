import math


class Node:
    def __init__(self, key=0, parent=None):
        self.key = key
        self.left = None
        self.right = None
        self.parent = parent


def insert(root, node):
    if root.key > node.key:
        if root.left is None:
            root.left = node
            node.parent = root
        else:
            insert(root.left, node)
    else:
        if root.right is None:
            root.right = node
            node.parent = root
        else:
            insert(root.right, node)

#######################################################


def tree_size(root):
    if root is None:
        return 0
    return 1 + tree_size(root.left) + tree_size(root.right)


def tree_max(root):
    if root is None:
        return math.inf

    if root.left is None and root.right is None:
        return root.key
    if root.left is None and root.right:
        return max(tree_max(root.right), root.key)
    if root.right is None and root.left:
        return max(tree_max(root.left), root.key)
    if root.left and root.right:
        return max(tree_max(root.left), tree_max(root.right), root.key)


def _check_BST(root):
    if root is None:
        return True, None, None

    if root.left is None and root.right is None:
        return True, root.key, root.key
    else:
        right_subtree = _check_BST(root.right)
        left_subtree = _check_BST(root.left)

        left_minimum = left_subtree[1] if left_subtree[1] else root.key
        left_maximum = left_subtree[2] if left_subtree[2] else root.key

        right_minimum = right_subtree[1] if right_subtree[1] else root.key
        right_maximum = right_subtree[2] if right_subtree[2] else root.key

        is_bst = (
            root.key <= right_minimum and
            root.key >= left_maximum and
            right_subtree[0] and
            left_subtree[0]
        )

        return (
            is_bst,
            min(root.key, right_minimum, left_minimum),
            max(root.key, right_maximum, left_maximum)
        )


def check_BST(root):
    return _check_BST(root)[0]


def _min_diff(root):
    if root is None:
        return math.inf, None, None

    if root.left is None and root.right is None:
        return math.inf, abs(root.key), abs(root.key)
    elif root.left and root.right:
        right_subtree = _min_diff(root.right)
        left_subtree = _min_diff(root.left)

        min_diff = min(
            abs(root.key - right_subtree[1]),
            abs(root.key - left_subtree[2]),
            abs(right_subtree[1] - left_subtree[2]),
            right_subtree[0],
            left_subtree[0],
        )

        minimum = min(root.key, right_subtree[1], left_subtree[1])
        maximum = min(root.key, right_subtree[2], left_subtree[2])

        return min_diff, minimum, maximum
    else:
        if root.left:
            left_subtree = _min_diff(root.left)

            min_diff = min(
                abs(root.key - left_subtree[2]),
                left_subtree[0],
            )

            minimum = min(root.key, left_subtree[1])
            maximum = min(root.key, left_subtree[2])

            return min_diff, minimum, maximum

        if root.right:
            right_subtree = _min_diff(root.right)

            min_diff = min(
                abs(root.key - right_subtree[1]),
                right_subtree[0],
            )

            minimum = min(root.key, right_subtree[1])
            maximum = min(root.key, right_subtree[2])

            return min_diff, minimum, maximum


def min_diff(root):
    return _min_diff(root)[0]


def _count_distinct(root):
    if root is None:
        return 0, {}

    if root.left is None and root.right is None:
        return 1, {root.key}
    else:
        if root.left and root.right:
            right_subtree = _count_distinct(root.right)
            left_subtree = _count_distinct(root.left)

            unique_keys = right_subtree[1].union(left_subtree[1])
            unique_keys.add(root.key)
        else:
            if root.left:
                left_subtree = _count_distinct(root.left)
                unique_keys = left_subtree[1].union({root.key})

            if root.right:
                right_subtree = _count_distinct(root.right)
                unique_keys = right_subtree[1].union({root.key})

        unique_keys_num = len(unique_keys)
        return unique_keys_num, unique_keys


def count_distinct(root):
    return _count_distinct(root)[0]

#################################################


if __name__ == "__main__":
    T = Node(3)
    insert(T, Node(1))
    insert(T, Node(2))
    print(tree_max(T))
    # should print True
    print(check_BST(T))
    # should print 1
    print(min_diff(T))
    print(count_distinct(T))
