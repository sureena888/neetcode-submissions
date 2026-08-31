class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_nums = {}
        freq = [[] for i in range(len(nums)+1)]
        for num in nums:
            if num in freq_nums:
                freq_nums[num] += 1
            else:
                freq_nums[num] = 1
        for num, count in freq_nums.items():
            freq[count].append(num)
        
        top_k_results = []
        for i in range(len(freq)-1, 0, -1):
            for num in freq[i]:
                top_k_results.append(num)
                if len(top_k_results) == k:
                    return top_k_results


        