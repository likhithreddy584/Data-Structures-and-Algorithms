def print_number(n):
    if n % 3 == 0 and n % 5 == 0:
        print("likhithreddy")
    elif n % 3 == 0:
        print("likhith")
    elif n % 5 == 0:
        print("reddy")
    else:
        print(n)

print_number(3)
print_number(5)
print_number(10)