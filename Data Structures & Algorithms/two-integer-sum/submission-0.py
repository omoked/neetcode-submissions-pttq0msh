class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevHash = {} # track val:index

        for i, v in enumerate(nums):
            diff = target - v
            if diff in prevHash:
                return [prevHash[diff], i] # pair of indices
            prevHash[v] = i
        return