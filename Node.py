from random import *
from _service_data import *

class Node:
    def __init__(self, value, priority = float('Nan')):
        self.value = value
        # random priority from 0 to 1
        self.priority = priority
        if(priority == float('NaN')):
            self.priority = random()
        self.parent = None
        self.children = {'left': None, 'right': None}

    def _set_child(self, child):
        if (child._get_value() <= self.value) and self.children['left'] == None:
            self.children['left'] = child
        elif (child._get_value() > self.value) and self.children['right'] == None:
            self.children['right'] = child

    def _set_chosen_child(self, which, child):
        self.children[which] = child

    def check_full_children(self):
        if self.children['left'] == None or self.children['right'] == None:
            return False
        return True

    def _set_parent(self, parent):
        self.parent = parent

    def get_parent(self):
        return self.parent

    def get_children(self):
        return self.children

    def is_root(self, node):
        if self.parent == None:
            return True
        return False

    def is_left_child(self):
        if self.parent == None:
            return None
        # is this correct?
        elif self.parent._get_children()['left'] == self:
            return True
        else:
            return False

    def _set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def _set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def get_neighbour(self):
        if self.parent == None:
            return
        children = self.parent._get_children()
        if children['left'] == self:
            return children['right']
        elif children['right'] == self:
            return children['left']

    # new
    def get_chosen_child(self, which):
        return self.children[which]