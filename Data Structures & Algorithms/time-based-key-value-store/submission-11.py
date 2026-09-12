class TimeMap:

    def __init__(self):
        self.store=defaultdict(list) # name:[[value,time]]

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        lis=self.store[key]
        l,r,n=0,len(lis)-1,len(lis)
        res=''
        while l<=r:
            m=(l+r)//2
            if lis[m][1]==timestamp:
                return lis[m][0]
            elif lis[m][1]<timestamp:
                res=lis[m][0]
                l=m+1
            else:
                r=m-1
        return res
        