# 트리 : 루트노드, 단말노드(자식 노드가 없는 노드)
# 일반 트리 : 노드들이 임의의 개수와 자식을 가질 수 있는 트리 
# 이진 트리 : 자식 노드의 개수가 항상 2개 이하인 트리 
# 포화 이진 트리 : 각 레벨에 노드가 꽉 차있는 이진 트리 
# 완전 이진 트리 : 높이가 k인 트리에서 레벨 1부터 k-1까지 노드가 채워져 있고 마지막 레벨 k에서는 왼쪽부터 오른족 까지 순서대로 채워져 있는 이진트리를 말함 

# 링크 표현법 (왼쪽자식 -> data -> 오른쪽자식)

# 트리의 순회 : 전위 순회, 중위 순회, 후위 순회 

class TNode : # 이진 트리를 위한 노드 클래스  
    def __init__(self, data, left, right): # 생성자
        self.data = data
        self.left = left
        self.right = right

def preorder(n) : # 전위 순회
    if n is not None : 
        print(n.data, end = '') # 루트노드
        preorder(n.left) # 왼쪽
        preorder(n.right) # 오른쪽

def inorder(n) : # 중위 순회
    if n is not None : 
        inorder(n.left) # 왼쪽
        print(n.data, end= '') # 루트 노드
        inorder(n.right) # 오른쪽 

def postorder(n) : # 후위 순회
    if n is not None : 
        postorder(n.left) # 왼쪽
        postorder(n.right) # 오른쪽
        print(n.data, end= '') # 루트 노드

# 레벨 순회, 큐가 사용, 순환은 사용되지 않는다

from circular import *

def levelorder(root):
    queue = CircularQueue() # 큐 객체 초기화 
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue() # 큐에서 맨 앞의 노드 n을 꺼냄 
        if n is not None :
            print(n.data, end = '')
            queue.enqueue(n.left)
            queue.enqueue(n.right)
            
def count_node(n) : # 노드의 개수 구하기 
    if n is None : 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n) : # 단말 노드의 개수 구하기 
    if n is None : 
        return 0 
    elif n.left is None and n.right is None : 
        return 1 
    else :  
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n) :
    if n is None : 
        return 0 
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : # 더 높은 트리에 1을 더해서 반환 
        return hLeft + 1 
    else : 
        return hRight + 1 

table = [('A', '.-'), ('B', '-...'), ('C', '-.-.'), ('D', '-..'),
        ('E', '.'), ('F', '..-.'), ('G', '--.'), ('H', '....'),
        ('I', '..'), ('J', '.---'), ('K', '-.-'), ('L', '.-..'),
        ('M', '--'), ('N', '-.'), ('O', '---'), ('P', '.--.'),
        ('Q', '--.-'), ('R', '.-.'), ('S', '...'), ('T', '-'),
        ('U', '..-'), ('V', '...-'), ('W', '.--'), ('X', '-..-'),
        ('Y', '-.--'), ('Z', '--..') ]

class TNode : 
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def make_morse_tree():
    root = TNode( None, None, None)
    for tp in table : 
        code = tp[1] # 모르스 코드 
        node = root
        for c in code : 
            if c == '.' :
                if node.left == None : 
                    node. left = TNode (None, None, None)
                node = node.left
            elif c == '-' :
                if node.right == None : 
                    node.right = TNode(None, None, None)
                node = node.right

        node.data = tp[0]
    return root
        
def decode(root, code):
    node = root
    for c in code : 
        if c == '.' : node = node.left
        elif c == '-' : node = node.right
    return node.data

def encode(ch):
    idx = ord(ch)- ord('A') # 리스트에서 해당 문자의 인덱스 
    return table[idx][1]

# 최대 힙 : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리

class MaxHeap :
    def __init__ (self) :
        self.heap = [] # 리스트를 사용한 힙 
        self.heap.append(0)
    def size(self) : return len(self.heap) -1
    def isEmpty(self) : return self.size() == 0 
    def Parent(self, i) : return self.heap[i//2] # 부모 노드 반환
    def Left(self, i) : return self.heap[i*2] # 왼쪽 자식 반환
    def Right(self, i) : return self.heap[i*2+1] # 오른쪽 자식 반환
    def display(self, msg = '힙트리 : ') :
        print(msg, self.heap[1:])
    
    def insert(self,n) :
        self.heap.append(n) # 맨 마지막 노드에 삽입 
        i = self.size() # 노드 n의 위치
        while (i !=1 and n > self.Parent(i)): # 부모 노드 보다 크다면 
            self.heap[i] = self.Parent(i) # 부모를 끌어 내린다
            i = i//2 # 부모의 index로 
        self.heap[i] = n

    def delete(self) :
        parent = 1 
        child = 2 
        if not self.isEmpty() :
            hroot = self.heap[1]
            last = self.heap[self.size()]
            while (child <= self.size()):
                if child<self.size() and self.Left(parent)<self.Right(parent):
                    child += 1 
                if last >= self.heap[child] :
                    break
                self.heap[parent] = self.heap[child]
                parent = child
                child *= 2

            self.heap[parent] = last
            self.heap.pop(-1)
            return hroot


