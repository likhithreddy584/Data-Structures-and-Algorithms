def selection_sort(arr):
    """
    Selection Sort Algorithm
    
    Time Complexity:
    - Best Case: O(n²)
    - Average Case: O(n²)
    - Worst Case: O(n²)
    
    Space Complexity: O(1) - sorts in place
    
    Stable: No
    
    Note: Always performs O(n²) comparisons regardless of input
    """
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test)
    print("Sorted:", selection_sort(test.copy()))