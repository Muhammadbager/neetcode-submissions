class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        n = len(nums)

        for num in nums:
            counts[num] = 1 + counts.get(num, 0)

            if counts[num] > n // 2:
                return num
        return -1
