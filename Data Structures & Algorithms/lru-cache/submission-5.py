class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev,self.next=None,None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left,self.right=Node(0,0),Node(0,0)
        self.left.next,self.right.prev=self.right,self.left
        self.cache={} # key:Node

    def remove(self,Node):
        prev,nxt=Node.prev,Node.next
        prev.next=nxt
        nxt.prev=prev
    
    def insert(self,Node):
        mru=self.right.prev
        mru.next=Node
        Node.next=self.right
        Node.prev=mru
        self.right.prev=Node

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.left.next=lru.next
            lru.next.prev=self.left
            del self.cache[lru.key]
