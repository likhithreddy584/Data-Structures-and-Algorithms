def rotate_left(nums):
    first = nums[0]

    for i in range(len(nums) - 1):
        nums[i] = nums[i + 1]

    nums[-1] = first
    return nums


nums = [10, 20, 30, 40]
print("Rotated list:", rotate_left(nums))
