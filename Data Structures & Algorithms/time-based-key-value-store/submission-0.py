class TimeMap:

    def __init__(self):
        self.timemap = defaultdict(list) # key : val

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timemap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.timemap[key]) - 1
        res = ""
        while l <= r:
            m = (l + r) // 2
            tmstmp = self.timemap[key][m][1]
            if tmstmp > timestamp:
                r = m - 1
            elif tmstmp < timestamp:
                res = self.timemap[key][m][0]
                l = m + 1
            else:
                res = self.timemap[key][m][0]
                break
        return res
