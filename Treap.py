from Node import Node
from random import *

class Treap:
    def __init__(self):
        self.root = None
        self.n = 0 # Nodes number
        self.h = 0 # Tree hight ( can be usefull )
        self.values_list = [] # can be used to check our work
        self.values_dict = [] # contains pairs value:priority
        self.key_node_dict = {} # contains pairs key:Node

    def search(self, value):
        return None

    def __check_search(self, key, node):
        if(key in self.key_node_dict.keys()):
            real_node = self.key_node_dict[key]
        else:
            real_node = None
        if(node == real_node):
            return True
        else:
            return False

    def insert(self, value):
        node = Node(value)
        return node

    def delete(self, value):
        pass