#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import sys

"""""
for dirpath, dirnames, filenames in os.walk('/home/mario'):
    print ("Path: " + dirpath)
    print ("DirNames: " + str(dirnames))
    print ("FileNames: " + str(filenames))
"""""

"""""""""

def getPathDepth(absolute_path):
    return len(absolute_path.split('/')) - 1

directory = '/home/mario'

temp = []
initial_depth = getPathDepth(directory)

print "Initial Depth: " + str(initial_depth)

for dirpath, dirnames, filenames in os.walk('/home/mario'):
    temp.append(dirpath)
    for filename in filenames:
        temp.append(os.path.join(dirpath, filename))

for path in temp:
    print "Path: " + path

"""""""""

bar = '│   '
spaces = '    '
new_child = '├── '
last_new_child = '└── '


class Node:
    def __init__(self, depth, abs_path, parent):
        self.depth = depth
        self.children = []
        self.abs_path = abs_path
        self.parent = parent
        self.basename = os.path.basename(abs_path)

    def is_last_child(self):
        if self.parent.children[-1] == self:
            return True
        else:
            return False

    def sort_children(self):
        self.children.sort(key=lambda node: node.basename.lower())


class Counter:
    def __init__(self):
        self.n_files = 0
        self.n_directories = 0


def create_tree_rec(path, parent):
    if parent:
        # print "--Children Node Creation" + path
        if os.path.basename(path).startswith('.'):
            return
        node = Node(parent.depth + 1, path, parent)
        node.parent.children.append(node)
    else:
        # print ("Root Node Creation: " + path)
        node = Node(0, path, None)
    if os.path.isdir(path):
        # print 'Dir Node Creation'
        try:
            for entry in os.listdir(path):
                create_tree_rec(os.path.join(path, entry), node)
            node.sort_children()
        except OSError:
            pass

    return node


def print_tree(margin, root, counter):
    last_element = False
    for child in root.children:
        if not child.is_last_child():
            print(margin + new_child + child.basename)
        else:
            last_element = True
            print(margin + last_new_child + child.basename)
        if child.children:
            if last_element:
                print_tree(margin + spaces, child, counter)
            else:
                print_tree(margin + bar, child, counter)
        if os.path.isdir(child.abs_path):
            counter.n_directories += 1
        else:
            counter.n_files += 1


def main(path):
    root_node = create_tree_rec(path, None)
    print(path)
    counter = Counter()
    print_tree("", root_node, counter)
    print("\n" + str(counter.n_directories) + " directories, " + str(counter.n_files) + " files")


if __name__ == '__main__':
    if len(sys.argv) < 2:
        pathstr = "."
    else:
        pathstr = sys.argv[1]
    main(pathstr)
