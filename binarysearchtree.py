from binarynode import BinaryNode

class BinarySearchTree:
    def __init__(self):
        self._root = None
    
    def add(self, object):
        #create binary node of object
        bi_node = BinaryNode(object)
        #base case in tree is empty
        if self._root is None:
            self._root = bi_node
        else:
            try:
                self._rec_add(bi_node, self._root)
            except:
                print('The object "'+str(bi_node.entry)+ '" is a duplicate. Duplicates are not allowed.')

    def _rec_add(self, item, cur_node):
        if item == cur_node:
            raise ValueError
        if item > cur_node:
            if cur_node.right is None:
                cur_node.right = item
            else:
                self._rec_add(item, cur_node.right)
        if item < cur_node:
            if cur_node.left is None:
                cur_node.left = item
            else: 
                self._rec_add(item, cur_node.left)


    def pre_order(self):
        #Visit, LST, RST
        self._rec_pre_order(self._root)

    def _rec_pre_order(self, cur_node):
        if cur_node is not None:
            print(cur_node.entry)
            self._rec_pre_order(cur_node.left)

            self._rec_pre_order(cur_node.right)
                

    def in_order(self):
        #LST, Visit, RST
        self._rec_in_order(self._root)

    def _rec_in_order(self, cur_node):
        if cur_node is not None:
            self._rec_in_order(cur_node.left)
            print(cur_node.entry)
            self._rec_in_order(cur_node.right)

    def post_order(self):
        #LST, RST, Visit
        self._rec_post_order(self._root)

    def _rec_post_order(self, cur_node):
        if cur_node is not None:
            self._rec_post_order(cur_node.left)
            self._rec_post_order(cur_node.right)
            print(cur_node.entry)