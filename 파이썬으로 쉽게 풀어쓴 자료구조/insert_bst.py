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
