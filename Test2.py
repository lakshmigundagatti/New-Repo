# import combinations class
from itertools import combinations
# import string class
from Test import StringClass

# Create PairPossible class which is inherited by string class
# Child class
class PairPossibleClass(StringClass):

    # create method to find possible pairs from list
    def listOfPossiblePairs(self):
        input = self.convertStringToListOfChars()
        res = list(combinations(input, self.lengthOfString() - 1))
        self.output = []
        for i in res:
            self.output.append("".join(i))
        return self.output

    # create method to print pairs with space
    def printPairsWithSpace(self):
        l = pp.lengthOfString()
        a = " ".join(self.output)
        print(a)

# create object of class calling parametrized constructor
pp = PairPossibleClass("4321")

# print list
print(pp.convertStringToListOfChars())

# print possible pairs from list
listOfPossiblePair = pp.listOfPossiblePairs()
print(listOfPossiblePair)

# print pairs with space
pp.printPairsWithSpace()