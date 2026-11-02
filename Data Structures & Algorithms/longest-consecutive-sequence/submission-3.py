class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        

        for num in num_set:
            longest = 1
            if num - 1 not in num_set:
                length = 1

                while num + 1 in num_set:
                    length += 1
                    num += 1

                longest = max(longest, length)

            elif nums == []:
                longest=0
                return longest

        return longest