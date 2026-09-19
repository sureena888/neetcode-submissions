class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product_arr = [1]
        right_arr = 1

        for i in range(len(nums)-1):
            product_arr.append(product_arr[i] * nums[i])

        for i in range(len(nums)-1,-1,-1):
              product_arr[i] *= right_arr
              right_arr *= nums[i]
              
        return product_arr