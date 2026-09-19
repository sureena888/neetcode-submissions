class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = [1]
        right_arr = [1]

        for i in range(len(nums)-1):
            product_arr.append(product_arr[i] * nums[i])

        count = 0
        for i in range(len(nums)-1,0,-1):
              right_arr.append(right_arr[count] * nums[i])
              count += 1

        final_count = 0
        for i in reversed(right_arr):
              product_arr[final_count] *= i
              final_count += 1

        return product_arr