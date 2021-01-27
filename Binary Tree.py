from typing import Any, Callable
import pygame as pg


class BinaryNode:
    value: Any
    left_child: 'BinaryNode'
    right_child: 'BinaryNode'

    def is_leaf(self) -> bool:
        return True if not self.left_child and not self.right_child else False

    def add_left_child(self, value: Any):
        self.left_child = BinaryNode(value)

    def add_right_child(self, value: Any):
        self.right_child = BinaryNode(value)

    def traverse_in_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_in_order(visit)
        visit(self)
        if self.right_child:
            self.right_child.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        if self.left_child:
            self.left_child.traverse_post_order(visit)
        if self.right_child:
            self.right_child.traverse_post_order(visit)
        visit(self)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        visit(self)
        if self.left_child:
            self.left_child.traverse_pre_order(visit)
        if self.right_child:
            self.right_child.traverse_pre_order(visit)

    def __init__(self, value, left_child=None, right_child=None):
        self.left_child = left_child
        self.right_child = right_child
        self.value = value

    def __repr__(self):
        txt = '***********************\n'
        txt += f'Value : {self.value}\n'
        if self.left_child:
            txt += f'Left child:{self.left_child.value}\n'
        if self.right_child:
            txt += f'Right child:{self.right_child.value}\n'
        txt += '***********************'
        return txt


class BinaryTree:
    root: BinaryNode

    def traverse_in_order(self, visit: Callable[[Any], None]):
        self.root.traverse_in_order(visit)

    def traverse_post_order(self, visit: Callable[[Any], None]):
        self.root.traverse_post_order(visit)

    def traverse_pre_order(self, visit: Callable[[Any], None]):
        self.root.traverse_pre_order(visit)

    def show(self):
        HEIGHT = 900
        WIDTH = 1200
        r = True
        pg.font.init()
        pg.init()
        x = pg.display.set_mode((WIDTH, HEIGHT))

        while r:
            x.fill((55, 55, 55))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    r = False

            drawtree(600, 100, self.root, x)
            pg.display.flip()
            pg.time.Clock().tick(5)

    def __init__(self, root=None):
        self.root = BinaryNode(root)


def drawtree(startposx, startposy, node, surface, spread=200):
    g = pg.font.SysFont('Monospace', 15)
    txt = g.render(f'Node({node.value})', False, (200, 200, 200))
    surface.blit(txt, (startposx, startposy - 30))
    pg.draw.rect(surface, pg.color.Color(25, 105, 105), pg.Rect(startposx, startposy, 51, 51))

    if node.left_child:
        pg.draw.line(surface, pg.color.Color(65, 135, 0), (startposx + 25, startposy + 25),
                     (startposx - spread + 25, startposy + 125), 2)
        drawtree(startposx - spread, startposy + 100, node.left_child, surface, spread - 50)
    if node.right_child:
        pg.draw.line(surface, pg.color.Color(65, 135, 0), (startposx + 25, startposy + 25),
                     (startposx + spread + 25, startposy + 125), 2)
        drawtree(startposx + spread, startposy + 100, node.right_child, surface, spread - 50)


def visit(nodetovisit: BinaryNode = None):
    if nodetovisit:
        print(nodetovisit.value)


tree = BinaryTree(10)

tree.root.add_left_child(9)
tree.root.add_right_child(2)
tree.root.left_child.add_left_child(1)
tree.root.left_child.add_right_child(3)
tree.root.right_child.add_left_child(4)
tree.root.right_child.add_right_child(6)


assert tree.root.value == 10
assert tree.root.right_child.value == 2
assert tree.root.right_child.is_leaf() is False
assert tree.root.left_child.left_child.value == 1
assert tree.root.left_child.left_child.is_leaf() is True

print(tree.root)
# tree.root.traverse_in_order(visit)
tree.show()
