def reverse_list(nums):
    rev = []

    for i in range(len(nums) - 1, -1, -1):
        rev.append(nums[i])

    return rev


nums = [10, 20, 30, 40]
print("Reversed list:", reverse_list(nums))
