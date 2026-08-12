"""
Problem #001: Sort an Array
Difficulty: Easy
Tags: #arrays #sorting #built-in

Description
-----------
Given an array of integers, return the array sorted in ascending order.

You can use Python's built-in sorting methods for this problem.

Real-World Application:
Sorting is fundamental in programming - used in organizing data for display,
optimizing search operations, and preparing data for analysis.

Constraints
-----------
- 1 ≤ array.length ≤ 50,000
- -50,000 ≤ array[i] ≤ 50,000
- Time limit: 1 second
- Space limit: 256 MB

Examples
--------
Example 1:
Input: [64, 34, 25, 12, 22, 11, 90]
Output: [11, 12, 22, 25, 34, 64, 90]
Explanation: Array sorted in ascending order

Example 2:
Input: [5, 2, 3, 1]
Output: [1, 2, 3, 4, 5]
Explanation: Small array sorted

Example 3 (Edge Case):
Input: [1]
Output: [1]
Explanation: Single element array is already sorted

Example 4 (Negative Numbers):
Input: [-3, -1, -5, 0, 2]
Output: [-5, -3, -1, 0, 2]
Explanation: Works with negative numbers

Example 5 (Duplicates):
Input: [3, 1, 2, 1, 3]
Output: [1, 1, 2, 3, 3]
Explanation: Duplicates are maintained

Approach
--------
1. Use Python's built-in sorted() function or list.sort() method
2. sorted() returns a new sorted list (doesn't modify original)
3. list.sort() sorts in-place (modifies original list)
4. Both use Timsort algorithm (O(n log n) time complexity)

Hints
-----
Hint 1: Python has built-in sorting: sorted(array) or array.sort()

Hint 2: sorted() creates new list, .sort() modifies in-place

Hint 3: For descending order, use reverse=True parameter

Solution
--------
"""

# Approach 1: Using sorted() - Returns new list
def sort_array_v1(arr):
    """
    Sort array using sorted() built-in function.
    
    Time Complexity: O(n log n) - Timsort algorithm
    Space Complexity: O(n) - Creates new list
    
    Pros: Doesn't modify original array
    Cons: Uses extra space
    """
    return sorted(arr)


# Approach 2: Using .sort() - In-place sorting
def sort_array_v2(arr):
    """
    Sort array in-place using .sort() method.
    
    Time Complexity: O(n log n) - Timsort algorithm
    Space Complexity: O(1) - Sorts in-place
    
    Pros: No extra space needed
    Cons: Modifies original array
    """
    arr.sort()
    return arr


# Approach 3: Using custom key (advanced)
def sort_array_custom(arr):
    """
    Sort with custom comparisons.
    
    Example: Sort by absolute value
    """
    return sorted(arr, key=abs)


# Main solution (recommended)
def solve(arr):
    """
    Sort array in ascending order.
    
    Args:
        arr: List of integers to sort
        
    Returns:
        Sorted list in ascending order
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    """
    return sorted(arr)


"""
Detailed Explanation
-------------------

Python's sorted() and .sort() use Timsort:
- Hybrid of merge sort and insertion sort
- Stable sort (maintains order of equal elements)
- Performs well on real-world data
- Optimized for partially sorted data

Comparison:
-----------
sorted(arr):
    - Returns NEW sorted list
    - Original unchanged
    - Can sort any iterable
    - Use when: need to keep original

arr.sort():
    - Modifies list IN-PLACE
    - Returns None
    - Only works on lists
    - Use when: want to save space

Common Mistakes
--------------
1. ❌ Forgetting .sort() returns None:
   sorted_arr = arr.sort()  # Wrong! This is None
   
2. ❌ Trying to sort immutable types:
   tuple.sort()  # Error! Tuples can't be sorted in-place
   
3. ❌ Not handling empty arrays:
   Always check: if not arr: return []
   
4. ❌ Assuming sorted() sorts in-place:
   sorted(arr)  # Original arr unchanged!
   arr = sorted(arr)  # Correct way

5. ❌ Using bubble sort when not needed:
   Python's built-in is faster than manual implementations

Edge Cases Handled
------------------
✓ Empty array: []
✓ Single element: [42]
✓ Already sorted: [1, 2, 3, 4]
✓ Reverse sorted: [4, 3, 2, 1]
✓ Duplicates: [1, 1, 2, 2]
✓ Negative numbers: [-5, -1, 0, 3]
✓ All same: [5, 5, 5, 5]

Performance Notes
----------------
For small arrays (< 64 elements): Uses insertion sort
For larger arrays: Uses merge sort with optimizations
Best case: O(n) - already sorted
Average case: O(n log n)
Worst case: O(n log n)

Related Problems
---------------
- Sort Array by Parity (Easy)
- Sort Colors (Medium) - Dutch National Flag
- Custom Sort String (Medium)
- Merge Sorted Array (Easy)
- Largest Number (Medium)

Practice Tips
-------------
- Understand when to use sorted() vs .sort()
- Practice sorting with custom keys
- Learn about sort stability
- Compare with other sorting algorithms
- Try sorting by multiple criteria
"""

# Comprehensive Test Suite
def test_solve():
    """Test all edge cases and normal cases"""
    
    # Test 1: Normal case
    assert solve([64, 34, 25, 12, 22, 11, 90]) == [11, 12, 22, 25, 34, 64, 90]
    
    # Test 2: Small array
    assert solve([5, 2, 3, 1]) == [1, 2, 3, 5]
    
    # Test 3: Single element
    assert solve([42]) == [42]
    
    # Test 4: Empty array
    assert solve([]) == []
    
    # Test 5: Already sorted
    assert solve([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    
    # Test 6: Reverse sorted
    assert solve([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    
    # Test 7: Duplicates
    assert solve([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]
    
    # Test 8: Negative numbers
    assert solve([-3, -1, -5, 0, 2]) == [-5, -3, -1, 0, 2]
    
    # Test 9: All same
    assert solve([7, 7, 7, 7]) == [7, 7, 7, 7]
    
    # Test 10: Large numbers
    assert solve([1000, -1000, 500, -500, 0]) == [-1000, -500, 0, 500, 1000]
    
    print("✓ All 10 tests passed!")


# Interactive demonstration
def demonstrate():
    """Show different sorting scenarios"""
    print("="*60)
    print("Array Sorting Demonstrations")
    print("="*60)
    
    # Example 1: Basic sorting
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\n1. Basic sorting:")
    print(f"   Original: {arr1}")
    print(f"   Sorted:   {solve(arr1)}")
    
    # Example 2: Negative numbers
    arr2 = [-3, -1, -5, 0, 2]
    print(f"\n2. With negative numbers:")
    print(f"   Original: {arr2}")
    print(f"   Sorted:   {solve(arr2)}")
    
    # Example 3: Duplicates
    arr3 = [3, 1, 2, 1, 3]
    print(f"\n3. With duplicates:")
    print(f"   Original: {arr3}")
    print(f"   Sorted:   {solve(arr3)}")
    
    # Example 4: Descending order
    arr4 = [5, 2, 8, 1, 9]
    print(f"\n4. Descending order (reverse=True):")
    print(f"   Original:   {arr4}")
    print(f"   Descending: {sorted(arr4, reverse=True)}")
    
    print("\n" + "="*60)


if __name__ == "__main__":
    # Run tests
    test_solve()
    
    # Show demonstrations
    demonstrate()
    
    # Interactive example
    print("\n" + "="*60)
    print("Try your own array:")
    print("="*60)
    
    my_array = [45, 23, 67, 12, 89, 34]
    result = solve(my_array)
    print(f"Input:  {my_array}")
    print(f"Output: {result}")
