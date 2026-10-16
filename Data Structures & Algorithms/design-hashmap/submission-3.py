class MyHashMap:

    def __init__(self):
        # Initializes an empty Python dictionary
        self.map = {}

    def put(self, key: int, value: int) -> None:
        # Inserts or updates the key with the value
        self.map[key] = value

    def get(self, key: int) -> int:
        # Returns the value if key exists, otherwise returns -1
        return self.map.get(key, -1)

    def remove(self, key: int) -> None:
        # Removes the key if it exists in the map
        if key in self.map:
            del self.map[key]


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)