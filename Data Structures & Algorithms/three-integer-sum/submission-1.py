class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        final_sets = []

        for i, n in enumerate(nums):
            if i > 0 and n == nums[i-1]:
                continue
            needed = -1*n

            start = i+1
            end = len(nums) -1

            while start < end:
                while start < end and nums[start] + nums[end] > needed:
                    end -= 1
                while start < end and nums[start] + nums[end] < needed:
                    start += 1
                if start != end and nums[start] + nums[end] == needed:
                    final_sets.append([n, nums[start], nums[end]])
                    start += 1
                    while start < end and nums[start] == nums[start-1]:
                        start+=1
                    end -= 1
        return final_sets
        