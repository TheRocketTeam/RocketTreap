from random import *

class Node:
    def __init__(self, value, priority = float('Nan')):
        self.key = value
        # random priority from 0 to 1
        self.priority = priority
        if(priority == float('NaN')):
            self.priority = random()
        self.parent = None
        self.children = [None, None]
        # maybe it can be:
        # self.children = {left: None, right: None}

    def get_key(self):
        return self.key

    def get_priority(self):
        return self.priority

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def _set_child(self, child_num, child):
        self.children[child_num] = child

    def _set_parent(self, parent):
        self.parent = parent

    def _set_priority(self, priority):
        self.priority = priority

    def _get_priority(self):
        return self.priority
