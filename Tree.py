from typing import Any, List, Callable, Union
from plotly import *
import plotly as pl


class TreeNode:
    value: Any
    children: List['TreeNode']

    def is_leaf(self) -> bool:
        return True if not self.children else False

    def add(self, child: 'TreeNode') -> None:
        self.children.append(child)

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        if self.is_leaf():
            return
        else:
            for i in self.children:
                i.for_each_deep_first(visit)


    def for_each_level_order(self, visit: Callable[['TreeNode'], None]) -> None:
        pass

    def search(value: Any) -> Union['TreeNode', None]:
        pass

    def __init__(self, value, children=None):
        self.value = value
        self.children = children

    def __repr__(self):
        return str(self.value)


class Tree:
    root: TreeNode
    current: TreeNode

    def add(value: Any, parent_name: Any) -> None:
        pass

    def for_each_level_order(visit: Callable[['TreeNode'], None]) -> None:
        pass

    def for_each_deep_first(self, visit: Callable[['TreeNode'], None]) -> None:
        pass

    def __init__(self,root: 'TreeNode'= None):
        self.root = root
