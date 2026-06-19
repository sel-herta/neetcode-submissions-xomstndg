class MyHashSet:

    def __init__(self):
        self.hashSet = [False] * 1000000

    def add(self, key: int) -> None:
        self.hashSet[key] = True

    def remove(self, key: int) -> None:
        self.hashSet[key] = False

    def contains(self, key: int) -> bool:
        return self.hashSet[key]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)