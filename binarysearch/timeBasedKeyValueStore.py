class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        l, r = 0, len(self.dict[key]) - 1
        res = ""

        while l <= r:
            mid = l + (r - l) // 2

            if self.dict[key][mid][1] <= timestamp:
                l = mid + 1
                res = self.dict[key][mid][0]
            else:
                r = mid - 1
        
        return res


        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)