class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.idxhash = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.idxhash:
            return False
        else:
            self.data.append(val)
            self.idxhash[val] = len(self.data) - 1
            return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.idxhash:
            return False
        else:
            idx = self.idxhash[val]
            self.idxhash[self.data[-1]] = idx
            self.data[idx] = self.data[-1]
            self.data.pop()
            del self.idxhash[val]
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        i = random.randrange(0,len(self.data))
        return self.data[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()