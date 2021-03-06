#!/usr/bin/python
# -*- coding: utf-8 -*-

class DisjointSet(object):

    def __init__(self, size):
        # Create a new element with a unique id, a rank of 0
        self.rank = [0]*size

        # The parent pointer to itself indicates that element is the representative member of its own set
        self.parent = [i for i in range(size)]
        self.size = size

    def find(self, x):
        # It follows the chain of parent pointers from x up the tree until it reaches a root element
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        # Determine the roots of the trees x and y belong to
        x_root = self.find(x)
        y_root = self.find(y)

        #If the roots are not distinct
        if x_root == y_root:
            return

        # If the roots are distinct, the trees are combined by attaching the root of one
        # to the root of the other.
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root

        elif self.rank[y_root] < self.rank[x_root]:
            self.parent[y_root] = x_root

        else:
            self.parent[y_root] = x_root
            self.rank[x_root] = self.rank[x_root] + 1


if __name__ == '__main__':
    ds = DisjointSet(5)
    ds.union(0, 2)
    ds.union(4, 2)
    ds.union(3, 1)

    if ds.find(4) == ds.find(0):
        print('yes')
    else:
        print('no')

    if ds.find(1) == ds.find(0):
        print('yes')
    else:
        print('no')