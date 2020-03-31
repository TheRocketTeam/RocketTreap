# Python 3.6
from random import *


class Node:
    def __init__(self, value):
        self.key = value
        # random priority from 0 to 1
        self.priority = random()
        self.parent = None
        self.children = [None, None]
        # maybe it can be:
        # self.children = {left: None, right: None}

    def _set_child(self, child_num, child):
        self.children[child_num] = child

    def _set_parent(self, parent):
        self.parent = parent

    def _set_priority(self, priority):
        self.priority = priority

    def _get_priority(self):
        return self.priority

class Treap:
    def __init__(self):
        self.root = None
        self.n = 0 # Nodes number
        self.h = 0 # Tree hight ( can be usefull )
        self.values_list = [] # can be used to check our work
        self.values_dict = [] # contains pairs value:priority

    def search(self, value):
        return None

    def insert(self, value):
        node = Node(value)
        return node

    def delete(self, value):
        pass

if __name__ == '__main__':
    n = Node(5)
    print(n.priority)