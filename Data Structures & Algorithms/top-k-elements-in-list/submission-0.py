from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        result = []

        for item in count.most_common(k):
            result.append(item[0])

        return result