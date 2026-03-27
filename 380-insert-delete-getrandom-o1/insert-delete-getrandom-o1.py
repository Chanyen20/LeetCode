class RandomizedSet:

    def __init__(self):
        self.data_list = []
        self.index_map = dict()
        
    def insert(self, val: int) -> bool:
        if val not in self.index_map:
            self.data_list.append(val)
            self.index_map[val] = len(self.data_list) - 1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.index_map:
            last_value = self.data_list[-1]
            last_value_index = self.index_map[last_value]
            target_value_index = self.index_map[val]

            self.data_list[last_value_index], self.data_list[target_value_index] = self.data_list[target_value_index], self.data_list[last_value_index]

            self.index_map[last_value] = target_value_index
            del self.index_map[val]
            self.data_list.pop()
            return True
        else:
            return False  

    def getRandom(self) -> int:
        return random.choice(self.data_list)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()