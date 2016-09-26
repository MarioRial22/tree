#!/usr/bin/env python
import sys,os
from collections import defaultdict
# helpful hints https://en.wikipedia.org/wiki/Box-drawing_character

class Node(object):

    def __init__(self):
        self.name = ""
        self.metadata = {}
        self.children = []


class Tree(object):

    def __init__(self,root):
        """
        :param root: Root directory
        """
        self.root_node = Node()
        # Build the tree here
        pass

    def walk(self):
        """
        Walks starting from root and populates self.tree
        :return:
        """
        pass

    def __str__(self):
        """
        Print the tree representations
        :return:
        """
        return "Hello World"


def main(root,regex=None,collect_metadata=False):
    dir_tree = Tree(root)
    print(dir_tree)

if __name__ == '__main__':
    import os
    # main(sys.argv[1])
    # just for demo
    os.system('tree {}'.format(' '.join(sys.argv[1:])))