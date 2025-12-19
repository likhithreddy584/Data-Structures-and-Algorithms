def find_largest_smallest(nums):
    largest = nums[0]
    smallest = nums[0]

    for n in nums:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

    return largest, smallest


nums = [10, 45, 2, 99, 23]
largest, smallest = find_largest_smallest(nums)
print("Largest:", largest)
print("Smallest:", smallest)
