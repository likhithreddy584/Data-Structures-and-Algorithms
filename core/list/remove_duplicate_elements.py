def remove_duplicates(nums):
    unique = []

    for n in nums:
        if n not in unique:
            unique.append(n)

    return unique


nums = [1, 2, 2, 3, 4, 4, 5]
print("Unique list:", remove_duplicates(nums))

