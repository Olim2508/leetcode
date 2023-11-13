import math
from collections import defaultdict
from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        hash_map = defaultdict(list)
        for i, val in enumerate(list1):
            hash_map[val].append(i)

        for i, val in enumerate(list2):
            hash_map[val].append(i)
        res = defaultdict(list)
        min_index = float("inf")
        for k in hash_map:
            if len(hash_map[k]) > 1 and sum(hash_map[k]) <= min_index:
                sum_index = sum(hash_map[k])
                min_index = sum_index
                res[min_index].append(k)

        return res[min_index]

    def solution_from_net(self, list1: List[str], list2: List[str]) -> List[str]:
        words1 = {word: idx for idx, word in enumerate(list1)}

        min_sum = math.inf
        for idx2, word2 in enumerate(list2):
            if word2 in words1:
                if words1[word2] + idx2 < min_sum:
                    min_sum = words1[word2] + idx2
                    min_words = [word2]
                elif words1[word2] + idx2 == min_sum:
                    min_words.append(word2)

        return min_words


if __name__ == '__main__':
    s = Solution()
    assert s.findRestaurant(
        list1=["Shogun", "Piatti", "Tapioca Express", "Burger King", "KFC"],
        list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ) == ["Piatti"]

    assert s.findRestaurant(
        list1=["happy", "sad", "good"],
        list2=["sad", "happy", "good"]
    ) == ["happy", "sad"]

    assert s.findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]
    ) == ["Shogun"]

    assert s.findRestaurant(
        list1=["Shogun", "Tapioca Express", "Burger King", "KFC"],
        list2=["KFC", "Shogun", "Burger King"]
    ) == ["Shogun"]
