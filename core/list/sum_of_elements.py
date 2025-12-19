def list_sum(nums):
    total = 0

    for n in nums:
        total += n

    return total


nums = [5, 10, 15, 20]
print("Sum:", list_sum(nums))
