class StringClass:
    def __init__(self, value):
       self.value = value
    def length(self):
       return len(self.value)
    def tolist(self):
        list1 = []
        list1[:0] = self.value
        return list1
obj = StringClass("lakshmi")
print(obj.length())
print(obj.tolist())