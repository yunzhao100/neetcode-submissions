class TimeMap:

    def __init__(self):
        self.store=defaultdict(list) # name:[(time, value)]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp,value))

    def get(self, key: str, timestamp: int) -> str:
        list_=self.store[key]
        l,r=0,len(list_)-1
        res=''
        while l<=r:
            m=(l+r)//2
            if list_[m][0]<=timestamp:
                res=list_[m][1]
                l=m+1
            else:
                r=m-1
        return res
