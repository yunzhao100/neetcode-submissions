class TimeMap:

    def __init__(self):
        self.dic=defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key].append((value,timestamp))

    def get(self, key: str, timestamp: int) -> str:
        list_=self.dic[key]
        l,r=0,len(list_)-1
        res=''
        while l<=r:
            m=(l+r)//2
            if list_[m][1]<=timestamp:
                res=list_[m][0]
                l=m+1
            else:
                r=m-1
        return res
