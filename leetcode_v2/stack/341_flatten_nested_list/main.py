import unittest


# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: []):
        self.stack = []
        self.dfs(nestedList)
        self.stack.reverse()

    def dfs(self, nested):
        for n in nested:
            if isinstance(n, int):
                self.stack.append(n)
            else:
                self.dfs(n)

    def next(self) -> int:
        return self.stack.pop()

    def hasNext(self) -> bool:
        return len(self.stack) > 0


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())


class TestCase(unittest.TestCase):

    def test_example_1(self):
        input = [[1, 1], 2, [1, 1]]
        self.iterator = NestedIterator(input)
        output = []
        while self.iterator.hasNext():
            output.append(self.iterator.next())

        self.assertEqual(output, [1, 1, 2, 1, 1])

    def test_example_2(self):
        input = [1, [4, [6]]]
        self.iterator = NestedIterator(input)
        output = []
        while self.iterator.hasNext():
            output.append(self.iterator.next())

        self.assertEqual(output, [1, 4, 6])

    # def test_example_3(self):
    #     input = [[1, 1], 2, [1, 1]]
    #     self.iterator = NestedIterator(input)
    #     output = []
    #     while self.iterator.hasNext():
    #         output.append(self.iterator.next())
    #
    #     self.assertEqual(output, [1, 1, 2, 1, 1])


if __name__ == '__main__':
    unittest.main()