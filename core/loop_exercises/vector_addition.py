def vector_addition(list1, list2):

    if len(list1) != len(list2):
        raise ValueError("Both lists must be of the same length.")
    
    result = []

    for i in range(len(list1)):
        print(i)
        result.append(list1[i] + list2[i])

    return result


# Example
A = [1, 2, 3]
B = [4, 5, 6]



print(vector_addition(A, B))
