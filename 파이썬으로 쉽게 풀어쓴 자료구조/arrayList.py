class ArrayList : 
    def __init__(self) :
        self.items=[]
    def insert(self,pos, el) :
        self.items.insert(pos,el)
    def delete(self, pos) :
        self.items.pop(pos)
    def isEmpty(self):
        return self.size()==0
    def getEntry(self,pos) : 
        return self.items[pos]
    def size(self):
        return len(self.items)
    def clear(self):
        self.items=[]
    def find(self,el):
        return self.items.index(el)
    def replace(self,pos,el):
        self.items[pos]=el
    def sort(self):
        self.items.sort()

    def merge1(self,lst):
        self.items.extend(lst)
    def merge2(self, otherList):
        self.items.extend(otherList.items)
    def display(self, msg = 'ArrayList') :
        print(msg, "항목수=", self.size(), self.items)
