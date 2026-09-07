class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        start = 0
        last = len(nums) - 1

        while(start <= last):

            if(nums[start] % 2 != 0):
                temp = nums[start]
                nums[start] = nums[last]
                nums[last] = temp
                last -= 1

            else :
                start += 1
               
        return nums
