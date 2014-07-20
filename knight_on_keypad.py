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

def generate_node_pool():
    pool = {}
    for i in [1,2,3,4,6,7,8,9]:
        pool[i]=Node(i)
    return pool
    

class parentNode(object):
    
    def __init__(self, parentNode):
        self._parentNodes = parentNode
    
    def __repr__(self):
        return self._parentNodes
    
    def update_parent_nodes(self,parentNodes):
        self._parentNodes = [i for i in parentNodes]
    
    

def sentinal(parent_node):
    return len([i for i in parent_node.depth_first()])

def genrate_tree(node_root,parent_node):
#    print sentinal(parent_node)
    parent_node = node_root
    if sentinal(parent_node)<=3:
        [node_root.add_child(Node(i)) for i in jump[node_root._value]]
        print node_root._children[0],node_root._children[1]
        genrate_tree(node_root._children[0],parent_node)
        genrate_tree(node_root._children[1],parent_node)
    else:
        return

        

def get_root():
    return None

def get_child_nodes(root):
    return [Node(i) for i in jump.get(root)]
    
def update_children(root):
    childrens = get_child_nodes(root)
    [root.add_child(child) for child in childrens]
    
        
        
    

def main():
    root =  Node(1)
    parentNode([root])
    for i in range(9):    
        for node in parentNode._parentNodes:
            update_children(node)
            parentNode.update_parent_nodes(node._children)
    pprint.pprint(root.depth_first)
    
    
    
    

        
    
         
    
#    #1    
#    for j in tree_top._children:
#        [j.add_child(Node(i)) for i in jump[j._value]]
#    #2
#    for k in j._children:
#        [k.add_child(Node(i)) for i in jump[k._value]]
#    # 3
#    for l in k._children:
#        [l.add_child(Node(i)) for i in jump[l._value]]
#    #4
#    for m in l._children:
#        [m.add_child(Node(i)) for i in jump[m._value]]
#    #5
#    for n in m._children:
#        [n.add_child(Node(i)) for i in jump[n._value]]
#    return node_root
    
# Example
if __name__ == '__main__':
    main()
#    generate_node_pool()
#    node_root = Node(1)
#    sentinal_prime = sentinal(node_root)
#    tt = genrate_tree(node_root,node_root)
#    print tt.depth_first()
#    for ch in tt.depth_first():
#        print ch
    
#    root = Node(1)
#    child1 = Node(jump[root._value][0])
#    child2 = Node(jump[root._value][1])
#    root.add_child(child1)
#    root.add_child(child2)
#    child1.add_child(Node(jump[child1._value][0]))
#    child1.add_child(Node(jump[child1._value][1]))
#    child2.add_child(Node(jump[child2._value][0]))
#    child2.add_child(Node(jump[child2._value][1]))
#    print root,root._children
#    for ch in root.depth_first():
#        print ch

