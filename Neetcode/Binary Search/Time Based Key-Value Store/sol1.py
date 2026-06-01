class TimeMap:

    def __init__(self):
        self.dic = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dic[key] = self.dic.get(key, []) + [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dic:
            return ""

        lis = self.dic[key]
        
        l,r = 0, len(lis)-1

        ans = ""

        while l <= r:
            mid = l + (r-l)//2

            if lis[mid][1] <= timestamp:
                ans = lis[mid][0]
                l = mid + 1
            else:
                r = mid - 1

        return ans