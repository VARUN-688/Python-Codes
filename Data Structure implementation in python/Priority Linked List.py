class Node:
    def __init__(self,val,ne=None):
        self.val=val
        self.next=ne
class List:
    def __init__(self):
        self.head=None
        
        
    def create(self,val):
        return Node(val)
    
    
    def insert(self,val):
        
        if self.head==None:
            self.head=self.create(val)
            
        else:
            node=self.create(val)
            if node.val<self.head.val:
                node.next=self.head
                self.head=node
            else:
                cur=self.head
                prev=None
                while cur.val<node.val and cur!=None:
                    
                    prev=cur
                    cur=cur.next
                    if cur==None:
                        break
                prev.next=node
                node.next=cur
                
    def display(self):
        node=self.head
        while node!=None:
            print(node.val)
            node=node.next
        
            
