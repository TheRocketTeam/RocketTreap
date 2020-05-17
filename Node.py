from random import *
from _service_data import *

#################################
# TODO:
# _is_left_child returns three values: True, False, None. It's incorrect
#  ^ add check on root (or make root permanently left or right)
#  self._get_children() isn't private. It should be  self.get_children()


#################################

class Node:
    def __init__(self, value):
        global priority_range
        global priority_step

        self.value = value
        # Set priority to the node at random
        if priority_step == 'int':
            self.priority = randrange(priority_range)
        elif priority_step == 'float':
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

    def is_root(self):
        if self.parent == None:
            return True
        return False

    def is_left_child(self):
        # We conventionally agree that root is a right child
        if self.parent == None:
            return False
        elif self.parent.get_children()['left'] == self:
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

    def get_chosen_child(self, which):
        return self.children[which]

    # new
    def _is_leaf(self):
        if(self.children['left']==None and self.children['right']==None):
            return True
        return False