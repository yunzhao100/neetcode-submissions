class Node:
    def __init__(self,key,val):
        self.key,self.val=key,val
        self.prev=self.next=None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap=capacity
        self.cache={} # map key to node

        self.left, self.right=Node(0,0), Node(0,0) # two dummy nodes
        self.left.next,self.right.prev=self.right,self.left
    
    def remove(self,node):
        # remove any real node, not necessarily the most left one
        prev,nxt=node.prev,node.next
        prev.next,nxt.prev=nxt,prev

    def insert(self,node): 
        # insert to the most right of real nodes, and the next is the right dummy node
        prev,nxt=self.right.prev,self.right
        prev.next=nxt.prev=node
        node.next,node.prev=nxt,prev

    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key]) # the node still exists, only deleted from the dic
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key]=Node(key,value)
        self.insert(self.cache[key])

        if len(self.cache) > self.cap:
            lru=self.left.next
            self.remove(lru)
            del self.cache[lru.key]
