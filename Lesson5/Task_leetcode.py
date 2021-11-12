class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        temp_nums = set()
        for i in nums:
            if i > 0:
                temp_nums.add(i)

        for i in range(1, 2**31):
            if i not in temp_nums:
                num = i
                break

        return num