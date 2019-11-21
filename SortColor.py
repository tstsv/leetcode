class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        s = 0
        n = len(nums) - 1
        while (i <= n):
            if (nums[i] == 2 and n>i):
                while (nums[n]==2 and n>i):
                    n = n -1
                (nums[i], nums[n]) = self.letSwap(nums[i], nums[n])
            elif (nums[i] == 0):
                if (s < i):
                    (nums[i], nums[s]) = self.letSwap(nums[i], nums[s])
                s = s + 1
                i = i + 1
            else:
                i = i + 1
            #print('s = ' + str(s) + ' i = ' + str(i) + ' n = ' + str(n))
            #print(*nums)
            
    def letSwap(self, a, b):
        return (b, a)
