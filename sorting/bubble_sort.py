def bubble_sort(arr):
    """
    Bubble Sort Algorithm - Detailed Explanation
    
    Time Complexity:
    - Best Case: O(n) - when array is already sorted (no swaps made)
    - Average Case: O(n²)
    - Worst Case: O(n²) - when array is reverse sorted
    
    Space Complexity: O(1) - sorts in place
    Stable: Yes
    """
    
    made_swap = True  
    n = len(arr)    
    
    
    while made_swap:
        made_swap = False 
        
        
        
        for i in range(n - 1):
            
            if arr[i] > arr[i + 1]:
                
                temp = arr[i]           
                arr[i] = arr[i + 1]     
                arr[i + 1] = temp       
                
                
                made_swap = True
    
    return arr


if __name__ == "__main__":
    test = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", test)
    print("Sorted:", bubble_sort(test.copy()))
    
   