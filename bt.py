import collections

class BinaryTree:
    '''A bifurcating arborescence.'''

    label = None
    _left = None
    _right = None
    _parent = None
    
    def __init__(self, label, left=None, right=None):
        if not label:
            return ValueError("Must specify label")
        self.label = label
        self.set_left(left)
        self.set_right(right)

    def _assign_child(self, side, child):
        if child:
            if not isinstance(child, BinaryTree):
                raise ValueError("Child must be a binary tree.")
            child._parent = self
            if side == "left":
                self._left = child
            elif side == "right":
                self._right = child
            else:
                raise ValueError("Invalid position")

    def __repr__(self):
        return str(self.to_tuple())
        
    def to_tuple(self):
        left = self.left().to_tuple() if self.left() else None
        right = self.right().to_tuple() if self.right() else None
        tpl = (self.label, left, right)
        if tpl == (None, None, None):
            return None
        if left == None and right == None:
            return self.label
        return tpl
            
    def set_left(self, l=None):
        self._assign_child("left", l)

    def left(self):
        return self._left

    def set_right(self, r):
        self._assign_child("right", r)

    def right(self):
        return self._right

    def parent(self):
        return self._parent

    def _DFS(self, label):
        if self.label == label:
            return self
        else:
            if self.left():
                left = self.left()._DFS(label)
                if left:
                    return left
            if self.right():                
                right = self.right()._DFS(label)
                if right:
                    return right
            return False

    def exists(self, label):
        if self._DFS(label):
            return True
        else:
            return False

    def distance(self, label):
        result = self._DFS(label)
        if not result:
            raise ValueError("Label '{}' does not exist in tree".format(label))
        distance = 0
        parent = result.parent()
        while True:
            if parent == None:
                return distance
            parent = parent.parent()
            distance += 1

    def path(self, label):
        result = self._DFS(label)
        if not result:
            raise ValueError("Label '{}' does not exist in tree".format(label))
        path = [result.label]
        parent = result.parent()
        while True:
            if parent == None:
                return path
            path.append(parent.label)
            parent = parent.parent()

    def levels(self, cur_level = 0, max_level = None):
        '''Done via DFS to be a pest'''
        levels = {cur_level: 1}
        left = right = {}
        left_max = right_max = 0
        if self.left():
            left = self.left().levels(cur_level+1, max_level)
            if left:
                left_max = max(left.keys())
        if self.right():
            right = self.right().levels(cur_level + 1, max_level)
            if right:
                right_max = max(right.keys())
        deepest = max(left_max, right_max)
        for level in xrange(cur_level + 1, deepest + 1):
            levels[level] = left.get(level, 0) + right.get(level, 0)
        return levels

    
def build(t):
    if t is None:
        return None
    tree = None
    if isinstance(t, collections.Sequence):
        tree = BinaryTree(t[0], build(t[1]), build(t[2]))
    else:
        tree = BinaryTree(t)
    return tree
        
            
    
            

    
        
