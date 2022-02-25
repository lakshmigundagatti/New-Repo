import Test3
import Test
import Test2

# create EqualSumPairsClass to find length of list and sum of elements of list
class EqualSumPairsClass:
    # Get 2 lists from string class and PairsPossible class
    my_list1 = Test.listOfChar
    my_list2 = Test2.listOfPossiblePair

    # create function to find the length of list
    def getLengthOfList(self, list):
        # Finding length of list using loop
        # Initializing counter
        counter = 0
        for i in list:
            # incrementing counter
            counter = counter + 1
        # Printing length of list
        print("Length of list is : " + str(counter))

    # create function to find sum of elements of list
    def getSumOfPairsNumbers(self, list):
        list_int = []
        total = 0
        # convert list of string into list of integer
        for element in list:
            list_int.append(int(element))
        # print integer list
        print(list_int)
        # using for loop, get sum of elements of list
        for ele in range(0, len(list_int)):
            # sum of numbers
            total = total + list_int[ele]
        # print sum of list of elements
        print("Sum of all elements in given list: ", total)

# create object of EqualSumPairsClass
equalSumPair = EqualSumPairsClass()

# print length of list of string class
equalSumPair.getLengthOfList(EqualSumPairsClass.my_list1)

# print sum of elements of list of string class
equalSumPair.getSumOfPairsNumbers(EqualSumPairsClass.my_list1)

# print length of list of PairsPossible class
equalSumPair.getLengthOfList(EqualSumPairsClass.my_list2)

# print sum of elements of list of PairsPossible class
equalSumPair.getSumOfPairsNumbers(EqualSumPairsClass.my_list2)

# print output of SearchCommonElements class
Test3.SearchCommonElementsClass.common_member(EqualSumPairsClass.my_list1, EqualSumPairsClass.my_list2)