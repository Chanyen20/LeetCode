class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res_product = []
        
        left_product = 1
        for num in nums:
            res_product.append(left_product)
            left_product *= num

        right_product = 1
        for i in range(len(nums) - 1, -1, -1):
            res_product[i] *= right_product
            right_product *= nums[i]
        
        return res_product
        



        