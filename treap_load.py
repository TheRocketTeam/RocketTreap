from Treap import Treap
from Node import Node
import pandas as pd
import math

def example_reader(filename):
    df = pd.read_csv(filename)
    df = df.set_index('key')
    dict_gr = df.to_dict(orient='index')
    treap = example_tree_creation(dict_gr)
    return treap

def example_tree_creation(DICT):
    print(DICT)
    root = float('nan')
    for key in DICT.keys():
        if (DICT[key]['root'] == True):
            root = key

    treap = Treap()
    root_node = Node(root, DICT[root]['priority'])
    treap.root, treap.key_node_dict, treap.h = recursive_build(DICT, root_node, {}, 0)
    treap.n = len(DICT.keys())
    print(treap.key_node_dict)
    return treap

def recursive_build(DICT, cur_node:Node, key_node_dict:dict, hight:int):
    max_hight = hight
    key = cur_node.get_value()
    key_node_dict[key] = cur_node

    l_child_key = DICT[key]['l_child']
    if(math.isnan(l_child_key)):
        l_child = None
        cur_node._set_chosen_child('left', None)
    else:
        print(l_child_key)
        print(type(l_child_key))
        l_child = Node(l_child_key, DICT[l_child_key]['priority'])
        l_child, key_node_dict, max_hight = recursive_build(DICT, l_child, key_node_dict, hight+1)
        l_child._set_parent(cur_node)
    cur_node._set_chosen_child('left', l_child)

    r_child_key = DICT[key]['r_child']
    if(math.isnan(r_child_key)):
        r_child = None
    else:
        r_child = Node(r_child_key, DICT[r_child_key]['priority'])
        r_child, key_node_dict, max_hight = recursive_build(DICT, r_child, key_node_dict, hight+1)
        r_child._set_parent(cur_node)
    cur_node._set_chosen_child('right', r_child)

    return cur_node, key_node_dict, max_hight

