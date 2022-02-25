class StringClass:
    pass
class PairsPossible(StringClass):
    def possiblePairs(self):
        test_list = self.list1
        res = list(Combinations(test_list, self.length() - 1))
        # res = [(a,b) for idx, a in enumerate(test_list) for b i test_list[idx + 1]]
        self.pairs = []
        # print(res)
        for i in res:
        self.pairs.append("".join(i))
        return self.pairs
         a = " ".join(self.pairs)
            print(a)
            obj = PairsPossible("lakshmi")
            print(obj.tolist())
            print(obj.possiblePairs())