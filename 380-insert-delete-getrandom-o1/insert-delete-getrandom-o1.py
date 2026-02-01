class RandomizedSet:

    def __init__(self):
        self.data = []
        self.mapping = dict()
        

    def insert(self, val: int) -> bool:
        if val in self.mapping:
            return False
        else:
            self.data.append(val)
            n = len(self.data)
            self.mapping[val] = n - 1           
            return True

    def remove(self, val: int) -> bool:
        if val in self.mapping:
            index = self.mapping[val]
            last_element = self.data[-1]
            self.data[index] = last_element
            self.mapping[last_element] = index
            del self.mapping[val]
            self.data.pop()
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.data)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()