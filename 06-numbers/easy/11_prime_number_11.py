"""
Problem #003: Check if Number is Prime
Difficulty: Easy
Tags: #numbers #math #prime #optimization

Description
-----------
Determine whether a given positive integer is a prime number.

A prime number is a natural number greater than 1 that has no positive 
divisors other than 1 and itself. For example: 2, 3, 5, 7, 11, 13...

Real-World Application:
Prime numbers are fundamental in cryptography (RSA encryption), hashing 
algorithms, random number generation, and computer security.

Constraints
-----------
- 1 ≤ n ≤ 10^9
- Time limit: 1 second
- Space limit: 256 MB

Examples
--------
Example 1:
Input: 7
Output: True
Explanation: 7 has no divisors other than 1 and 7

Example 2:
Input: 12
Output: False
Explanation: 12 = 2 × 6, so it's composite

Example 3 (Edge Case - Small):
Input: 2
Output: True
Explanation: 2 is the smallest and only even prime

Example 4 (Edge Case - One):
Input: 1
Output: False
Explanation: 1 is not considered prime by definition

Example 5 (Large Prime):
Input: 97
Output: True
Explanation: 97 is prime (no divisors from 2 to 96)

Approach
--------
1. Handle edge cases (n ≤ 1, n == 2, even numbers)
2. Check divisors only up to √n for efficiency
3. Use 6k±1 optimization for even faster checking

Hints
-----
Hint 1: No need to check beyond √n (if n = a×b, one must be ≤ √n)

Hint 2: Handle edge cases: numbers ≤ 1 are not prime, 2 is prime

Hint 3: After checking 2, only check odd divisors (skip evens)

Solution
--------
"""

import math


# Approach 1: Optimized (check up to √n)
def is_prime_optimized(n):
    """
    Check divisors only up to √n.
    
    Time: O(√n)
    Space: O(1)
    
    Best for: Most cases
    """
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    
    return True


# Approach 2: 6k±1 optimization
def is_prime_advanced(n):
    """
    Use 6k±1 pattern for faster checking.
    
    Time: O(√n)
    Space: O(1)
    
    All primes > 3 are of form 6k±1
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


# Main solution
def solve(n):
    """
    Check if a number is prime.
    
    Args:
        n: Positive integer to check
        
    Returns:
        True if prime, False otherwise
    
    Time Complexity: O(√n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    
    return True


"""
Common Mistakes
--------------
1. ❌ Forgetting that 1 is not prime
2. ❌ Not handling 2 (the only even prime)
3. ❌ Checking all numbers up to n (too slow)
4. ❌ Not handling negative numbers

Edge Cases
----------
✓ n = 1: False
✓ n = 2: True (only even prime)
✓ Even numbers > 2: False
✓ Large primes: True

Related Problems
---------------
- Count Primes (Easy)
- Prime Factorization (Medium)
"""

# Test Suite
def test_solve():
    assert solve(1) == False
    assert solve(2) == True
    assert solve(3) == True
    assert solve(7) == True
    assert solve(12) == False
    assert solve(97) == True
    print("✓ All 6 tests passed!")


if __name__ == "__main__":
    test_solve()
    print(f"\n7 is prime: {solve(7)}")
    print(f"12 is prime: {solve(12)}")
