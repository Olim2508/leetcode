import unittest
from typing import List


class TimeMap:

    def __init__(self):
        self.time_values: dict = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.time_values:
            self.time_values[key].append([value, timestamp])
        else:
            self.time_values[key] = [[value, timestamp]]

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.time_values.get(key, [])

        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            print("values[mid][1]", values[mid][1])
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                l = mid + 1
            else:
                r = mid - 1
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)


class TestCase(unittest.TestCase):
    def setUp(self):
        self.obj = TimeMap()

    def test_example_1(self):
        self.obj.set("foo", "bar", 1)
        res = self.obj.get("foo", 1)
        self.assertEqual(res, "bar")

        res = self.obj.get("foo", 3)
        self.assertEqual(res, "bar")

        self.obj.set("foo", "bar2", 4)
        res = self.obj.get("foo", 4)
        self.assertEqual(res, "bar2")

        res = self.obj.get("foo", 5)
        self.assertEqual(res, "bar2")

    # def test_example_2(self):
    #     key = ""
    #     value = ""
    #     timestamp = 1
    #     self.obj.set(key, value, timestamp)
    #     res = self.obj.get(key, timestamp)
    #     self.assertEqual(res, 4)


if __name__ == '__main__':
    unittest.main()
