def count_letters_digits(text):
    letters = 0
    digits = 0

    for ch in text:
        if ch.isalpha():
            letters += 1
        elif ch.isdigit():
            digits += 1

    return letters, digits


# Input from user
s = input("Enter a string: ")

# Function call
letters, digits = count_letters_digits(s)

# Output
print("Letters:", letters)
print("Digits:", digits)
