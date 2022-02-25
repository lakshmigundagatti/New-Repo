# Create StringClass
# Parent class
class StringClass:

    # Create constructor to take input
    def __init__(self, input):
        # Enter String in digits form like E.g.- 11563456
        self.input = input

    # Create method which returns length of String
    def lengthOfString(self):
        return len(self.input)

    # This method converts string into list of characters and print it in list
    def convertStringToListOfChars(self):
        list1 = []
        list1[:0] = self.input
        return list1

# Create object of StringClass
str1 = StringClass("1234")

# Print length of string
print("Length of string is: ", str1.lengthOfString())

# Print list of characters in string
listOfChar = str1.convertStringToListOfChars()
print("List of characters: ", listOfChar)