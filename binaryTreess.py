# -*- coding: utf-8 -*-
"""
Binary Trees
February 2016
@author: Nathalie
"""

# Helpers
from algoQueue import *

# Binary Tree class
class BinTree:
    '''
    define the name
    '''

# Binary Tree factory helper function
def newBinTree(key, left, right):
    B = BinTree()
    B.key = key
    B.left = left
    B.right = right
    return B

# Example Binary Trees
B_ex = newBinTree(1, 
          newBinTree(2, 
                newBinTree(4, newBinTree(8,None,None), None), 
                newBinTree(5,None,newBinTree(11,None,None))),
          newBinTree(3, 
                newBinTree(6,None,None), 
                newBinTree(7, newBinTree(14,None,newBinTree(29,None,None)),None)))
         
B_tuto = newBinTree('V', 
            newBinTree('D', 
               newBinTree('I', 
                  newBinTree('Q', None,newBinTree('U', None,None)),
                  None),
               newBinTree('S', 
                  newBinTree('E', None,None),
                  newBinTree('T', None,None))),
            newBinTree('I', 
               newBinTree('E', 
                  None,
                  newBinTree('R', None,None)),
              newBinTree('A', 
                  newBinTree('T', None,None),
                  newBinTree('S', None,None))))         

def printTree(B, s=""):
    '''
    display from GolluM/Nath
    '''
    if B == None:
        print(s, '- ')
    elif B.left == None and B.right == None:
        print(s, '- ', B.key)
    else:
        print(s, '- ', B.key)
        printTree(B.left, s + "  |")
        printTree(B.right, s + "   ")
        
#------------------------------------------------------------------------------
"""    
1 - Measures
"""
            
def size(B):
    if B == None:
        return 0
    else:
        return 1 + size(B.left) + size(B.right)

def height(B):
    if B == None:
        return -1
    else:
        return 1 + max(height(B.left), height(B.right))


def epl(B, h = 0):
    '''
    Binary Tree External Path Length
    Returns: (EPL, Leaf count)
    '''
    if B == None:
        return (0, 0)
    elif B.left == None and B.right == None:
        return (h, 1)
    else:
        (a, n1) = epl(B.left, h+1)
        (b, n2) = epl(B.right, h+1)
        return (a + b, n1 + n2)

def ead(B):
    '''
    Binary Tree External Average Depth
    '''
    if B == None:
        raise Exception("Empty tree")
    else:
        (p, n) = epl(B)
        return p / n

# Alternate versions with leaf count passed as an int list ref
def epl2(B, n, h = 0):
    if B == None:
        return 0
    elif B.left == None and B.right == None:
        n[0] = n[0] + 1
        return h
    else:
        return epl2(B.left, n, h+1) + epl2(B.right, n, h+1)

def ead2(B):
    if B == None:
        raise Exception("Empty tree")
    else:
        n = [0]
        return epl2(B, n) / n[0]

#------------------------------------------------------------------------------
"""    
2.1 - Depth-First Traversals
"""

def depthPrefix(B):
    '''
    Depth-first traversal
    Prints keys in preorder
    '''
    if B != None:
        print(B.key, end=' ')
        depthPrefix(B.left)
        depthPrefix(B.right)
        
def depthInfix(B):
    '''
    Depth-first traversal
    Prints keys in inorder
    '''
    if B != None:
        depthInfix(B.left)
        print(B.key, end=' ')
        depthInfix(B.right)

def depthSuffix(B):
    '''
    Depth-first traversal
    Prints keys in postorder
    '''
    if B != None:
        depthInfix(B.left)
        depthInfix(B.right)
        print(B.key, end=' ')


def tree2Abstract(B):
    '''
    Prints the "abstract" form of the tree
    '''
    if B == None:
        print('_', end='')
    else:
        print('<', end='')
        tree2Abstract(B.left)
        print(B.key, end='')
        tree2Abstract(B.right)
        print('>', end='')

def tree2AbstractStr(B):
    '''
    Returns the "abstract" form of the tree as a string
    '''
    if B == None:
        return '_'
    else:
        s = '<' + str(B.key) + ','
        s = s + tree2AbstractStr(B.left) + ','
        s = s + tree2AbstractStr(B.right)
        s = s + '>'
        return s

def tree2AbstractStr2(B):
    if B == None:
        return '_'
    else:
        return '<' + str(B.key) + ',' \
        + tree2AbstractStr2(B.left) + ',' \
        + tree2AbstractStr2(B.right) + '>'

"""    
2.2 - Breadth-First Traversals
"""

def breadth(B):
    '''
    Prints keys in breadth-first traversal order
    '''
    q = enqueue(B, newQueue())
    while not isEmpty(q):
        T = dequeue(q)
        print(T.key, end=' ')
        if T.left != None:
            q = enqueue(T.left, q)
        if T.right != None:
            q = enqueue(T.right, q)
    
def width(B):
    q = enqueue(B, newQueue())
    q = enqueue(None, q)
    w = 0
    max_w = 0
    while not isEmpty(q):
        T = dequeue(q)
        if T == None:
            max_w = max(max_w, w)
            w = 0
            if not isEmpty(q):
                q = enqueue(None, q)
        else:
            w = w + 1
            if T.left != None:
                q = enqueue(T.left, q)
            if T.right != None:
                q = enqueue(T.right, q)
    return max_w


#----------------------------------------------------------------------

# tests
def testBinTree(B):
    printTree(B)
    print("Depth-First Traversals:")
    print("----------------------")
    print("- Preorder:", end = ' ')
    depthPrefix(B)
    print()
    print("- Inorder:", end = ' ')
    depthInfix(B)
    print()
    print("- Postorder:", end = ' ')
    depthSuffix(B)
    print()
    print(tree2AbstractStr(B))
    print()
    print("Breadth-First Traversal:")
    print("-----------------------")
    breadth(B)
    print('\n')
    print("size =", size(B), "- height =", height(B), \
        "- external average depth =", ead(B), "- width =", width(B))
