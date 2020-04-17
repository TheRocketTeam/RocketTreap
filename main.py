# Python 3.6

from Treap import Treap
from Node import Node
from treap_load import example_reader

#################################
# TODO:



#################################


if __name__ == '__main__':
    filename = 'treap_ex1.csv'
    treap = example_reader(filename)
    print(f'HEIGHT: {treap.h}')
    treap.normal_print(treap.root)
    search_res = treap.search(6)
    if(search_res!=None):
        print(search_res.priority)

    treap.delete(7)
    treap.normal_print(treap.root)
