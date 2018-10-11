# remove all 0 to the end of the list
# without copy the original list

class Solution:
    def moveZeroes(self, nums):
        size, newInd = len(nums), 0
        for i in range(size):
            if nums[i] != 0:
                nums[newInd] = nums[i]  #其实就是将K个不为零的数移到前k位（k < len(list)）
                newInd += 1
        nums[newInd:] = [0] * (size - newInd)
