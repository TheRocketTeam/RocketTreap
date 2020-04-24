from Node import Node
from random import *
from _service_data import *

#################################
# TODO:
# Add meld function from here: https://www.youtube.com/watch?v=erKlLEXLKyY
# Rotations work wrong (deletion of 7 isn't correct)
# _is_left_child


#################################

class Treap:
    def __init__(self, priority_range = 1, heap_kind = 'max'):
        self.root = None
        self.n = 0 # Nodes number
        self.h = 0 # Tree hight ( can be usefull )
        self.values_list = [] # can be used to check our work
        self.values_dict = {} # contains pairs value:priority
        self.priority_range = priority_range
        self.heap_kind = heap_kind

    ###########################################
    ### S E A R C H       F U N C T I O N S ###
    ###########################################

    def __rec_search(self, cur_node, value):
        """
        Recursive search implementation
        :param cur_node: current node
        :param value: searched value
        :return: ...
        """
        if(cur_node == None):
            return None
        if(cur_node.value == value):
            return cur_node
        elif(cur_node.value < value):
            return self.__rec_search(cur_node.get_chosen_child('right'), value)
        elif (cur_node.value > value):
            return self.__rec_search(cur_node.get_chosen_child('left'), value)

    def search(self, value):
        """
        Search function implementation
        :param value: searched value
        :return: node with searched value if it exists, None otherwise
        """
        search_res = self.__rec_search(self.root, value)
        if(search_res == None):
            print(f"Node with key {value} not found")
        else:
            print(f"Node with key {value} found.")
        return search_res

    def right_rotation(self, node_y):

        # get the data about our root
        y_parent = node_y.get_parent()
        y_children = node_y.get_children()
        x = y_children['left']
        if x!= None:
            x_children = x.get_children()
            t_2 = x_children['right']
        else:
            t_2 = None

        # make x the root of the subtree we are working with
        if node_y.is_left_child():
            y_parent._set_chosen_child('left', x)
        elif not node_y.is_left_child() and y_parent != None:
            y_parent._set_chosen_child('right', x)
        x._set_parent(y_parent)

        # reattache right child of x (t_2) to be left child of y
        if t_2 != None:
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
        if y != None:
            y_children = y.get_children()
            t_2 = y_children['left']
        else:
            t_2 = None


        # make y the root of the subtree we are working with
        if node_x.is_left_child():
            x_parent._set_chosen_child('left', y)
        elif not node_x.is_left_child() and x_parent != None:
            x_parent._set_chosen_child('right', y)
        y._set_parent(x_parent)

        # reattache left child of y (t_2) to be right child of y
        if(t_2 != None):
            t_2._set_parent(node_x)
        node_x._set_chosen_child('right', t_2)

        # make x a child of y
        node_x._set_parent(y)
        y._set_chosen_child('left', node_x)
        return


    ###########################################
    ### I N S E R T       F U N C T I O N S ###
    ###########################################


    def insert(self, value, rand_range):
        node = Node(value)
        # If the tree is empty, set this node as a root
        if self.root == None:
            self.root = node
        else:
            # We will always work with two nodes - one given and one with which we are comparing the given one
            comparing_node = self.root
            # At forst we want to insert the new node to be a leaf
            while not comparing_node._is_leaf():
                if comparing_node.get_value() >= value:
                    comparing_node = comparing_node.get_chosen_child('left')
                elif comparing_node.get_value() < value:
                    comparing_node = comparing_node.get_chosen_child('right')
            if comparing_node.get_value() >= value:
                comparing_node._set_chosen_child('left', node)
            elif comparing_node.get_value() < value:
                comparing_node._set_chosen_child('right', node)
            node._set_parent(comparing_node)
        # Perform rotations until we are max/min heap (currently done for max)
        if self.heap_kind == 'max':
            while node.get_priority() > comparing_node.priority():
                if node.is_left_child():
                    self.right_rotation(comparing_node)
                elif not node.is_left_child():
                    self.left_rotation(comparing_node)
                if not node.is_root():
                    comparing_node = node.get_parent()
                else:
                    return
        elif self.heap_kind == 'min':
            while node.get_priority() < comparing_node.priority():
                if node.is_left_child():
                    self.right_rotation(comparing_node)
                elif not node.is_left_child():
                    self.left_rotation(comparing_node)

                if not node.is_root():
                    comparing_node = node.get_parent()
                else:
                    return
        return


    ###########################################
    ### D E L E T E       F U N C T I O N S ###
    ###########################################

    def __rec_delete(self, del_candidate : Node):
        # If node is now a leaf:
        if (del_candidate._is_leaf()):
            parent = del_candidate.get_parent()
            if (del_candidate.is_left_child()):
                parent._set_chosen_child('left', None)
            else:
                parent._set_chosen_child('right', None)
            del del_candidate
        # If node is not a leaf, but has only one child
        elif(not del_candidate.check_full_children()):

            parent = del_candidate.get_parent()

            child = del_candidate.get_chosen_child('left')
            if(child == None):
                child = del_candidate.get_chosen_child('right')

            if (del_candidate.is_left_child()):
                parent._set_chosen_child('left', child)
            else:
                parent._set_chosen_child('right', child)

            child._set_parent(parent)

            del del_candidate

        # If node has two children
        else:
            del_candidate._set_priority(n_inf)
            l_child = del_candidate.get_chosen_child('left')
            r_child = del_candidate.get_chosen_child('right')

            if(l_child.get_priority() > r_child.get_priority()):
                self.right_rotation(del_candidate)
            else:
                self.left_rotation(del_candidate)
            self.__rec_delete(del_candidate)


    def delete(self, value):
        del_candidate = self.search(value)
        if(del_candidate==None):
            print(f"Node with key {value} not found.")
        else:
            self.__rec_delete(del_candidate)
            print(f"Node with key {value} was deleted")

    ###########################################
    ### S E R V I C E     F U N C T I O N S ###
    ###########################################

    def check_hight(self):
        pass

    def _set_priority_range(self, range):
        self.priority_range = range

    def _set_heap_kind(self, kind):
        self.heap_kind = kind

    ###########################################
    ### P R I N T I N G   F U N C T I O N S ###
    ###########################################

    def normal_print(self, node, _prefix="", _right=True):
        """
        Prints tree in hierarchical view
        :param node: root of the branch that you wish to print
        :param _prefix: printing parameter
        :param _right: should be True if current node is right son
        :return:
        """
        if (node == None):
            return

        line = _prefix
        if (_right):
            line += "`- "
        else:
            line += "|- "
        line += '(' + color.BOLD + str(node.value) + color.END + ', ' + str(node.priority) + ')'
        print(line)

        _prefix += "   " if _right else "|  "

        children = node.get_children()
        self.normal_print(children['left'], _prefix, False)
        self.normal_print(children['right'], _prefix, True)

    # Pretty print functions
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
        Prints tree as graph
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


