import unittest
from typing import List


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        secret_counts = {}
        guess_counts = {}

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_counts[secret[i]] = secret_counts.get(secret[i], 0) + 1
                guess_counts[guess[i]] = guess_counts.get(guess[i], 0) + 1

        # Second pass to count cows based on the minimum occurrences of matching digits in secret and guess
        for digit in secret_counts:
            if digit in guess_counts:
                cows += min(secret_counts[digit], guess_counts[digit])

        return f"{bulls}A{cows}B"


class TestCase(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_example_1(self):
        secret = "1807"
        guess = "7810"
        result = self.solution.getHint(secret, guess)
        self.assertEqual(result, "1A3B")

    def test_example_2(self):
        secret = "1123"
        guess = "0111"
        result = self.solution.getHint(secret, guess)
        self.assertEqual(result, "1A1B")


if __name__ == '__main__':
    unittest.main()
