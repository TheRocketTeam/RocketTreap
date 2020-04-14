from Node import Node
from random import *

class Treap:
    def __init__(self):
        self.root = None
        self.n = 0 # Nodes number
        self.h = 0 # Tree hight ( can be usefull )
        self.values_list = [] # can be used to check our work
        self.values_dict = [] # contains pairs value:priority

    def search(self, value):
        return None

    def right_rotation(self, node_y):

        # get the data about our root
        y_parent = node_y.get_parent()
        y_children = node_y.get_children()
        x = y_children['left']
        x_children = x.get_children()
        t_2 = x_children['right']

        # make x the root of the subtree we are working with
        if node_y.is_left_child():
            y_parent._set_chosen_child('left', x)
        elif not node_y.is_left_child():
            y_parent._set_chosen_child('right', x)
        x._set_parent(y_parent)

        # reattache right child of x (t_2) to be left child of y
        t_2._set_parent(node_y)
        node_y._set_chosen_child('left', t_2)

        # make y a child of x
        node_y._set_parent(x)
        x._set_chosen_child('right', node_y)
        return

    def left_rotation(self, node_x):

        # get the data about our root
        x_parent = node_x.get_parent()
        x_children = node_x.get_children()
        y = x_children['right']
        y_children = y.get_children()
        t_2 = y_children['left']


        # make y the root of the subtree we are working with
        if node_x.is_left_child():
            x_parent._set_chosen_child('left', y)
        elif not node_x.is_left_child():
            x_parent._set_chosen_child('right', y)
        y._set_parent(x_parent)

        # reattache left child of y (t_2) to be right child of y
        t_2._set_parent(node_x)
        node_x._set_chosen_child('right', t_2)

        # make x a child of y
        node_x._set_parent(y)
        y._set_chosen_child('left', node_x)
        return

    def insert(self, value):
        node = Node(value)
        return node

    def delete(self, value):
        pass

    # new functions
    def check_hight(self):
        pass

    def __check_empty_layer(self, layer_nodes):
        for node in layer_nodes:
            if(node != None):
                return False
        return True

    def __get_next_layer(self, layer_nodes):
        layer_descendants = []
        for node in layer_nodes:
            if(node == None):
                layer_descendants.append(None)
                layer_descendants.append(None)
            else:
                layer_descendants.append(node.get_chosen_child('left'))
                layer_descendants.append(node.get_chosen_child('right'))
        return layer_descendants

    def __cell_view(self, node):
        if(node == None):
            line = f"( None, None )"
        else:
            line = f"( {node.get_value()}, {node.get_priority()} )"
        while(len(line)<21):
            line = ' ' + line + ' '
        if(len(line)>21):
            line = line[:-1]
        cell_view = line
        return cell_view



    def __print_layer(self, layer_nodes, current_layer, occupied_windows):
        layer_windows = []
        for i in range(1, 2**(self.h+1)):
            # todo: check height - current_layer > 0
            if( i % (2 ** (self.h - current_layer)) == 0 and
                i not in occupied_windows):
                layer_windows.append(i)
                occupied_windows.add(i)
        # print(f'current_layer: {current_layer}')
        # print(f'layer_windows: {layer_windows}')
        row_line = ''
        upper_line = ''
        line = ''
        down_line = ''

        t = 0

        space = '     '
        over_flag = False
        for i in range(1, 2**(self.h+1)):
            if(i in layer_windows):
                if(over_flag == False):
                    over_flag = True
                    row_line += '          ___________'
                else:
                    over_flag = False
                    row_line += '___________          '

                upper_line += f'          |          '
                line += self.__cell_view(layer_nodes[t])
                t+=1
                down_line += f'          |          '
            else:
                if(over_flag == False):
                    row_line += f"{space}"
                else:
                    row_line += '_' * len(space)
                upper_line += f'{space}'
                line += f'{space}'
                down_line += f'{space}'

        if(current_layer != 0 ):
            print(row_line)
        print(upper_line)
        print(line)
        print(down_line)
        return occupied_windows



    def pretty_print(self):
        """
            recursive BFS run to print pretty
        :return: None
        """
        if(self.root == None):
            print("Empty tree")
        else:
            print("Pretty print:")
            height = self.h
            layer_nodes = [self.root]
            current_layer = 0
            occupied_windows = set()
            while(not self.__check_empty_layer(layer_nodes)):
                occupied_windows = self.__print_layer(layer_nodes, current_layer, occupied_windows)
                layer_nodes = self.__get_next_layer(layer_nodes)
                current_layer += 1

            print('done')


