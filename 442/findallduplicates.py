class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        # "Must write an algorithm that runs in O(n) time with O(1) extra space"
        def dup_iter():
            for n in nums:
                elem = abs(n) - 1
                if nums[elem] > 0:
                    nums[elem] = -nums[elem]
                else:
                    yield elem + 1
        # The max list length is notably less than 10**5, so it is technically O(1) space
        return list(dup_iter())
