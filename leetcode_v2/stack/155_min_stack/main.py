import unittest


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_values = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_values or self.min_values[-1] >= val:
            self.min_values.append(val)

    def pop(self) -> None:
        head_element = self.stack.pop()
        if head_element == self.min_values[-1]:
            self.min_values.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_values[-1]


class TestCase(unittest.TestCase):

    def test_example_1(self):
        self.stack = MinStack()
        self.stack.push(0)
        self.stack.push(1)
        self.stack.push(0)
        self.assertEqual(self.stack.getMin(), 0)
        self.stack.pop()
        self.assertEqual(self.stack.getMin(), 0)


if __name__ == '__main__':
    unittest.main()
