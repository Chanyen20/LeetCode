# class Solution:
#     def jump(self, nums: List[int]) -> int:
       
#         n = len(nums)

#         if n <= 1:
#             return 0

#         for i in range(n):
#             steps = i + nums[i]
#             if steps >= n - 1:
#                 return 1 + self.jump(nums[: i + 1])


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # 停止條件：如果在起點就是終點，步數為 0
        if n <= 1:
            return 0
        
        # 你的邏輯：從左邊開始找第一個能跳到終點的人
        for i in range(n):
            if i + nums[i] >= n - 1:
                # 找到了！這就是倒數第二站。
                # 接下來只要算「跳到 i 需要幾步」+ 這一跳 (1)
                return 1 + self.jump(nums[:i + 1])

        