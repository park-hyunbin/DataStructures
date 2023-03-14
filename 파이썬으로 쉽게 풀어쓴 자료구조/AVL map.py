class BSTNode : 
    def __init__(self,key,value) :
        self.key = key
        self.value = value
        self.left = None
        self.right = None

def count_node(n) :
    if n is None : 
        return 0 
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) :
    if n is None : 
        return 0 
    elif n.left is None and n.right is None : 
        return 1 
    else : 
        return count_leaf(n.left) + count_leaf(n.right)
        
def calc_height(n) :
    if n == None : return 0 
    hleft = calc_height(n.left)
    hright = calc_height(n.right)
    return (max(hleft,hright) + 1)

def calc_height_diff(n) :
    if n == None : return 0 
    return calc_height(n.left) - calc_height(n.right)

def levelorder(n) :
    que = []
    que.append(n)
    while len(que) != 0:
        node = que.pop(0)
        if node is not None : 
            print(node.key, end='')
            que.append(node.left)
            que.append(node.right)

def search_bst(n, key) :
    if n == None : 
        return None 
    elif key == n.key :
        return n 
    elif key < n.key :
        return search_bst(n.left,key)
    else : 
        return search_bst(n.right,key)
    
def search_value_bst(n, value):
    if n == None : return None
    elif value == n.value :
        return n 
    res = search_value_bst(n.left,value)
    if res is None : 
        return res
    else : 
        return search_value_bst(n.right, value)
def search_max_bst(n) :
    while n!= None and n.right != None :
        n = n.right
    return n

def search_min_bst(n) :
    while n!= None and n.left != None :
        n= n.left
    return n


def delete_bst_case1 (parent, node, root) :
    if parent is None :
        root = None
    else :
        if parent.left == node :
            parent.left = None
        else :
            parent.right = None
    return root

def delete_bst_case2 (parent, node, root) :
    if node.left is not None :
        child = node.left
    else :
        child = node.right
    if node == root :
        root = child
    else :
        if node is parent.left :
            parent.left = child
        else :
            parent.right = child
    return root

def delete_bst_case3 (parent, node, root) :
    succp = node
    succ = node.right
    while (succ.left != None) :
        succp = succ
        succ = succ.left

    if succp.left == succ :
        succp.left = succp.right
    else :
        succp.right = succ.right
    node.key = succ.key
    node.value = succ.value
    node = succ

    return root

def delete_bst (root, key) :
    if root == None : return None

    parent = None
    node = root
    while node != None and node.key != key:
        parent = node
        if key < node.key : node = node.left
        else : node = node.right
    if node == None : return None
    if node.left == None and node.right == None :
        root = delete_bst_case1 (parent, node, root)
    elif node.left== None or node.right== None :
        root = delete_bst_case2 (parent, node, root)
    else :
        root = delete_bst_case3 (parent, node, root)
    return root             

def insert_bst(r,n):
    if n.key < r.key :
        if r.left is None :
            r.left = n
            return True
        
        else :
            return insert_bst(r.left, n)
        
    elif n.key > r.key:
        if r.right is None :
            r.right = n
            return True
        
        else :
            return insert_bst(r.right, n)
    else :
        return False 
        
class BSTMap():
    def __init__(self):
        self.root = None

    def isEmpty (self) : return self.root == None
    def clear(self) : self.root == None
    def size(self) :return count_node(self.root)
    
    def search(self,key) : return search_bst(self.root,key)
    def searchValue(self,key) : return search_value_bst(self.root,key) 
    def findMax(self) : return search_max_bst(self.root)
    def findMin(self) : return search_min_bst(self.root)
    def insert(self,key,value = None) :
        n = BSTNode(key, value)
        if self.isEmpty() :
            self.root = n
        else :
            insert_bst(self.root,n)

    def delete(self,key):
        self.root = delete_bst(self.root,key)


def rotateLL(A) :
    B = A.left
    A.left = B.right
    B.right = A
    return B

def rotateRR(A) :
    B = A.right
    A.right = B.left
    B.left = A
    return B
def rotateRL(A) :
    B = A.right 
    A.right = rotateLL(B)
    return rotateRR(A)

def rotateLR(A) :
    B = A.left
    A.left = rotateRR(B)
    return rotateLL(A)

def reBalance(parent) :
    hDiff = calc_height_diff(parent)

    if hDiff > 1 :
        if calc_height_diff(parent.left) > 0 : 
            parent = rotateLL(parent)
        else : 
            parent = rotateLR(parent)
    elif hDiff < -1 :
        if calc_height_diff(parent.right) < 0 :
            parent = rotateRR(parent)
        else : 
            parent = rotateRL(parent)
    return parent

def insert_avl(parent, node) :
    if node.key < parent.key :
        if parent.left != None : 
            parent.left = insert_avl(parent.left,node)
        else : 
            parent.left = node
        return reBalance(parent)

    elif node.key > parent.key :
        if parent.right != None : 
            parent.right = insert_avl(parent.right, node)
        else : 
            parent.right = node
        return reBalance(parent)
    else : 
        print("중복된 키 에러")

        
class AVLMap(BSTMap) :
    def __init__(self) :
        super().__init__()

    def insert (self, key, value = None) :
        n = BSTNode(key, value)
        if self.isEmpty() :
            self.root = n 
        else : 
            self.root = insert_avl(self.root, n)

    def display(self, msg = 'AVLMap : ') :
        print(msg, end = '')
        levelorder(self.root)
        print()

node = [0,1,2,3,4,5,6,7,8,9]
map = AVLMap()

for i in node :
    map.insert(i)
    map.display("AVL(%d): "%i)

print(" 노드의 개수 = %d" % count_node(map.root))
print(" 단말의 노드 = %d" % count_leaf(map.root))
print(" 트리의 높이 = %d" % calc_height(map.root))
