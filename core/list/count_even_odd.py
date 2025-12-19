def count_even_odd(nums):
    even = odd = 0

    for n in nums:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1

    return even, odd


nums = [1, 2, 3, 4, 5, 6]
even, odd = count_even_odd(nums)
print("Even:", even)
print("Odd:", odd)
