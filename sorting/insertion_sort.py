def insertion_sort(arr):
    """
    Insertion Sort Algorithm
    
    Time Complexity:
    - Best Case: O(n) - when array is already sorted
    - Average Case: O(n²)
    - Worst Case: O(n²) - when array is reverse sorted
    
    Space Complexity: O(1) - sorts in place
    
    Stable: Yes
    
    Note: Performs well on small arrays and nearly sorted data
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test)
    print("Sorted:", insertion_sort(test.copy()))