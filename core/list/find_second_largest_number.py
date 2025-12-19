def second_largest(nums):
    largest = second = -1

    for n in nums:
        if n > largest:
            second = largest
            largest = n
        elif n > second and n != largest:
            second = n

    return second


nums = [10, 45, 23, 99, 67]
print("Second largest:", second_largest(nums))
