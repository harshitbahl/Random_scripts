# -*- coding: utf-8 -*-
"""
Created on Tue Jul 15 19:42:53 2014

@author: harshitbahl
"""


jump = {0: [6, 4], 1: [6, 8], 2: [9, 7],
            3: [4, 8], 4: [9, 3, 0], 6: [7, 1, 0],
            7: [6, 2], 8: [3, 1], 9: [4, 2]}
import pprint

class Node(object):
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
#        return 'Node({0})'.format(self._value)
        return str(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield [i for i in c.depth_first()]

class parentNode(object):
    
    def __init__(self, parentNode):
        self._parentNodes = parentNode
    
    def __repr__(self):
        return str(self._parentNodes)
    
    def update_parent_nodes(self,parentNodes):
        for new_parents in parentNodes:
            self._parentNodes.append(new_parents)
    
    def refresh(self):
        self._parentNodes  = []
        
    
    

def get_root():
    return None

def get_child_nodes(root):
    return [Node(i) for i in jump.get(root._value)]
    
def update_children(root):
    childrens = get_child_nodes(root)
    [root.add_child(child) for child in childrens]


    
# Example
if __name__ == '__main__':
    root =  Node(1)
    parent_nodes = parentNode([root])
    for i in range(5):
        #lets clean the parentnode and create copy
        parent_node_copy = parent_nodes._parentNodes
        # Reset the parenode Class
        parent_nodes.refresh()
        for node in parent_node_copy:
#            print 'Parent Node Copy', parent_node_copy
            update_children(node)
            parent_nodes.update_parent_nodes(node._children)
    pprint.pprint([ch for ch in root.depth_first()])





