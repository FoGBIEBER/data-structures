from BST import *


def rotateLL(A):
    B = A.left
    A.left = B.right
    B.right = A
    return B


def rotateRR(A):
    B = A.right
    A.right = B.left
    B.left = A
    return B


def rotateRL(A):
    B = A.right
    A.right = rotateLL(B)
    return rotateRR(A)


def rotateLR(A):
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)


def reBalance(parent):
    hDiff = calc_height_diff(parent)

    if hDiff > 1:
        if calc_height_diff(parent.left) > 0:
            parent = rotateLL(parent)
        else:
            parent = rotateLR(parent)
    elif hDiff < -1:
        if calc_height_diff(parent.right) < 0:
            parent = rotateRR(parent)
        else:
            parent = rotateRL(parent)
    return parent


def calc_height_diff(n):
    if n == None:
        return 0
    return calc_height(n.left) - calc_height(n.right)


def calc_height(n):
    if n == None:
        return 0
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    return (max(hleft, hright)+1)


def insert_avl(parent, node):
    if node.key < parent.key:
        if parent.left != None:
            parent.left = insert_avl(parent.left, node)
        else:
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key:
        if parent.right != None:
            parent.right = insert_avl(parent.right, node)
        else:
            parent.right = node
        return reBalance(parent)
    else:
        print("중복된 키 에러")


class AVLMap(BSTMap):
    def __init__(self):
        super().__init__()

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            self.root = insert_avl(self.root, n)

    def display(self, msg='AVLMap: '):
        print(msg, end='')
        levelorder(self.root)
        print()


if __name__ == '__main__':
    node1 = [7, 8, 9, 2, 1, 5, 3, 6, 4]
    map1 = AVLMap()

    for i in node1:
        map1.insert(i)
        map1.display('AVL({}): '.format(i))

    print(' 노드의 개수 = {}'.format(count_node(map1.root)))
    print(' 단말의 개수 = {}'.format(count_leaf(map1.root)))
    print(' 트리의 높이 = {}'.format(calc_height(map1.root)))
    print()

    node2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    map2 = AVLMap()

    for i in node2:
        map2.insert(i)
        map2.display('AVL({}): '.format(i))

    print(' 노드의 개수 = {}'.format(count_node(map2.root)))
    print(' 단말의 개수 = {}'.format(count_leaf(map2.root)))
    print(' 트리의 높이 = {}'.format(calc_height(map2.root)))
