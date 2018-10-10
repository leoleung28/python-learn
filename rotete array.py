def rotate1(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    k %= len(nums)  #取余数，如K超出数组的长度，如len = 6 , k = 8,则实际上只需要算 K = 2的情况即可
    nums[:] = nums[-k:]+nums[:-k]
    return (nums)
arr = [1,2,3,4,5,6]
v = 4
res = rotate1(arr,v)
print (res)

# example: arr[1,2,3,4,5,6] , k = 4
# result : [3,4,5,6,1,2]