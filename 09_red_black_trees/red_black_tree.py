import random
from enum import IntEnum

from ods.binarysearchtree import BinarySearchTree


class Color(IntEnum):
    red = 0
    black = 1


class RedBlackTree(BinarySearchTree):
    # NOTE: self.r: Root, self.nil: External node
    class Node(BinarySearchTree.Node):
        def __init__(self, color: Color, x):
            super().__init__(x)
            self.color = color

    def __init__(self, iterable=[]):
        # NOTE: External node is black
        self.nil = RedBlackTree.Node(Color.black, None)
        super().__init__(iterable=[], nil=self.nil)
        self.r = self.nil.right = self.nil.left = self.nil.parent = self.nil
        self.add_all(iterable)

    def rotate_left(self, u: Node):
        super().rotate_left(u)

    def rotate_right(self, u: Node):
        super().rotate_right(u)

    def push_black(self, u: Node):
        u.color -= 1
        u.left.color += 1
        u.right.color += 1

    def pull_black(self, u: Node):
        u.color += 1
        u.left.color -= 1
        u.right.color -= 1

    def swap_colors(self, u, v):
        v.color, u.color = u.color, v.color

    def is_root(self, u):
        return u == self.r

    def flip_left(self, u: Node):
        self.swap_colors(u, u.right)
        self.rotate_left(u)

    def flip_right(self, u: Node):
        self.swap_colors(u, u.left)
        self.rotate_right(u)

    def add(self, x):
        u = self.__class__.Node(Color.red, x)
        u.left = u.right = u.parent = self.nil

        if self.add_node(u):
            self.add_fixup(u)
            return True

        return False

    def add_fixup(self, u: Node):
        # u is node for insertion
        # u is red at initial
        while u.color == Color.red:
            if self.is_root(u):
                # Only change to black
                u.color = Color.black
                return

            # w is parent
            w = u.parent
            if w.left.color == Color.black:
                # Flip node to keep left-leaning
                self.flip_left(w)
                u = w
                w = u.parent

            if w.color == Color.black:
                # There is no red-edge
                return

            # u is red and parent is red
            # g is grandparent
            g = w.parent
            if g.right.color == Color.black:
                self.flip_right(g)
                return

            # u is red and parent is red and grandparent is red
            # Change colors of parent and its siblings to black
            self.push_black(g)
            u = g

    def remove(self, x):
        pass

    def find(self, x):
        pass


if __name__ == '__main__':
    t = RedBlackTree()
    n = 100

    for k in range(5):
        for i in range(n):
            x = random.randrange(0, 5 * n)
            t.add(x)

    print('done.')
