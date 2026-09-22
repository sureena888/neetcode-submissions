class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        starting_set = set()

        for num in nums:
            if num-1 not in nums_set:
                starting_set.add(num)

        max_count = 0
        for starting in starting_set:
            counter = 1
            check_val = starting + 1
            while check_val in nums_set:
                counter += 1
                check_val += 1
            if counter > max_count:
                max_count = counter
        
            
        return max_count

