"""
Problem #002: Reverse a String
Difficulty: Easy
Tags: #strings #reverse #two-pointers #interview-favorite

Description
-----------
Write a function that reverses a string. The input string is given as a string.

Real-World Application:
String reversal is used in palindrome checks, text processing, data formatting,
and is a fundamental operation in many algorithms.

Constraints
-----------
- 0 ≤ string.length ≤ 100,000
- String consists of printable ASCII characters
- Time limit: 1 second
- Space limit: 256 MB

Examples
--------
Example 1:
Input: "hello"
Output: "olleh"
Explanation: Simple reversal of 5 characters

Example 2:
Input: "Python"
Output: "nohtyP"
Explanation: Case is preserved

Example 3 (Edge Case - Empty):
Input: ""
Output: ""
Explanation: Empty string returns empty string

Example 4 (Edge Case - Single):
Input: "A"
Output: "A"
Explanation: Single character remains same

Example 5 (With Spaces):
Input: "Hello World"
Output: "dlroW olleH"
Explanation: Spaces are also reversed

Approach
--------
1. Use Python's slicing notation [::-1] (most Pythonic)
2. Or use reversed() function with join
3. Or use two-pointer technique for interviews

Hints
-----
Hint 1: Python strings can be sliced: s[::-1] reverses a string

Hint 2: Two pointers: swap characters from both ends moving toward center

Hint 3: reversed() returns iterator, need to join: ''.join(reversed(s))

Solution
--------
"""

# Approach 1: Python Slicing (Most Pythonic)
def reverse_v1(s):
    """
    Time: O(n), Space: O(n)
    Best for: Production code
    """
    return s[::-1]


# Approach 2: Using reversed()
def reverse_v2(s):
    """
    Time: O(n), Space: O(n)
    Best for: Memory efficient
    """
    return ''.join(reversed(s))


# Approach 3: Two Pointers
def reverse_v3(s):
    """
    Time: O(n), Space: O(n)
    Best for: Interviews
    """
    chars = list(s)
    left, right = 0, len(chars) - 1
    
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    
    return ''.join(chars)


# Main solution
def solve(s):
    """
    Reverse a string.
    
    Args:
        s: String to reverse
        
    Returns:
        Reversed string
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    return s[::-1]


"""
Common Mistakes
--------------
1. ❌ Trying to modify string directly (strings are immutable)
2. ❌ Not handling empty string
3. ❌ Off-by-one in two pointers: while left <= right is wrong
4. ❌ Inefficient concatenation: result += char in loop

Edge Cases Handled
------------------
✓ Empty string: "" → ""
✓ Single character: "A" → "A"
✓ With spaces: "a b" → "b a"
✓ Palindrome: "noon" → "noon"

Related Problems
---------------
- Reverse Words in a String (Medium)
- Valid Palindrome (Easy)
- Reverse String II (Medium)
"""

# Test Suite
def test_solve():
    assert solve("hello") == "olleh"
    assert solve("Python") == "nohtyP"
    assert solve("") == ""
    assert solve("A") == "A"
    assert solve("Hello World") == "dlroW olleH"
    assert solve("12345") == "54321"
    print("✓ All 6 tests passed!")


if __name__ == "__main__":
    test_solve()
    print(f"\nExample: '{solve('Hello, World!')}')"
