class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {}
        for num in nums:
            if num in freq_nums:
                freq_nums[num] += 1
            else:
                freq_nums[num] = 1
        sorted_freq_nums = sorted(freq_nums, key=freq_nums.get, reverse=True)

        return sorted_freq_nums[:k]
        