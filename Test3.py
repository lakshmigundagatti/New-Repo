import Test2
import Test

# create SearchCommonElementsClass to find common pairs from two lists
class SearchCommonElementsClass:
    # a = list of string class
    # b = list of PairsPossible class
    a = Test.listOfChar
    b = Test2.listOfPossiblePair

    # create function to get common elements from both list
    def common_member(a, b):
        a_set = set(a)
        b_set = set(b)

        # comparing both strings
        if (a_set & b_set):
            print("Common elements between these 2 lists " + str(a) + " and " + str(b) + " are:- ")
            print(a_set & b_set)
        else:
            print("No common elements")

    # calling method to get common elements from both lists
    common_member(a,b)