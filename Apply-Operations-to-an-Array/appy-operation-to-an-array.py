class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = 2 * nums[i]
                nums[i+1] = 0
        holder = 0
        for seeker in range(len(nums)):
            if nums[seeker] != 0:
                nums[seeker], nums[holder] = nums[holder], nums[seeker]
                holder += 1
        return nums
            
        