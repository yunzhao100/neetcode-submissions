class TimeMap:

    def __init__(self):
        self.keystore=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.keystore[key].append([value,timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res=''
        store=self.keystore[key]
        l,r=0,len(store)-1
        while l<=r:
            m=(l+r)//2
            if store[m][1]>timestamp:
                r=m-1
            elif store[m][1]<timestamp:
                res=store[m][0]
                l=m+1
            else:
                return store[m][0]
        return res