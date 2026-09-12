class Node:
    def __init__(self,next=None,prev=None):
        self.next,self.prev=next,prev
        self.key,self.val=0,0

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.left,self.right=Node(),Node()
        self.left.next,self.right.prev=self.right,self.left
        self.cache={} #key:Node

    def remove(self,Node):
        prev,nxt=Node.prev,Node.next
        prev.next=nxt
        nxt.prev=prev
    
    def insert(self,Node):
        mru=self.right.prev
        mru.next=Node
        Node.prev=mru
        Node.next=self.right
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
        self.cache[key]=Node()
        self.cache[key].key,self.cache[key].val=key,value
        self.insert(self.cache[key])
        if len(self.cache)>self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
