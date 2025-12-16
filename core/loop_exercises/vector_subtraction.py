def vector_subtraction(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Both lists must be of the same length.")
    result = []

    for i in range(len(list1)):
        print(i)

        result.append(list1[i] - list2[i])

    return result


# Example
A = [10, 20, 30]
B = [1, 2, 3]

print("Vector Subtraction:", vector_subtraction(A, B))
