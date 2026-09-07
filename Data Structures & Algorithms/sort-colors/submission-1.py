class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i = 0
        nz = 0          # boundary for 0s (left pointer)
        nt = len(nums) - 1   # boundary for 2s (right pointer)

        while(i <= nt):
            if(nums[i] == 0):
                nums[i] = nums[nz]
                nums[nz] = 0
                nz += 1
                i += 1

            elif(nums[i] == 2):
                temp = nums[nt]
                nums[nt] = nums[i]
                nums[i] = temp
                nt -= 1

            else :
                i += 1

        return         
