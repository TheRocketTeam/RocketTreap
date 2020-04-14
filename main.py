# Python 3.6

from Treap import Treap
from Node import Node
from treap_load import example_reader

if __name__ == '__main__':
    filename = 'treap_ex1.csv'
    treap = example_reader(filename)
    print(f'HEIGHT: {treap.h}')
    treap.pretty_print()
