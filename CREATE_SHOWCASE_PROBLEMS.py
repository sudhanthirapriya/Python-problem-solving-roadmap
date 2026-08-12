"""
Script to create 20 showcase problems with complete solutions.

This script will create gold-standard problems to demonstrate repository quality.
Each problem will have:
- Detailed description
- Multiple examples with edge cases
- Progressive hints
- Multiple solution approaches
- Complete working code
- Comprehensive tests
- Complexity analysis
"""

SHOWCASE_PROBLEMS = [
    {
        "path": "05-strings/easy/01_reverse_string_1.py",
        "title": "Reverse a String",
        "difficulty": "Easy",
        "priority": 1
    },
    {
        "path": "06-numbers/easy/01_check_prime_1.py",
        "title": "Check if Number is Prime",
        "difficulty": "Easy",
        "priority": 2
    },
    {
        "path": "02-control-flow/easy/01_fizzbuzz_1.py",
        "title": "FizzBuzz",
        "difficulty": "Easy",
        "priority": 3
    },
    {
        "path": "01-python-basics/easy/01_var_assignment.py",
        "title": "Variable Assignment and Types",
        "difficulty": "Easy",
        "priority": 4
    },
    {
        "path": "11-dsa/easy/01_binary_search_1.py",
        "title": "Binary Search",
        "difficulty": "Easy",
        "priority": 5
    },
    {
        "path": "07-arrays/medium/01_two_sum_1.py",
        "title": "Two Sum",
        "difficulty": "Medium",
        "priority": 6
    },
    {
        "path": "05-strings/medium/01_longest_substring_1.py",
        "title": "Longest Substring Without Repeating",
        "difficulty": "Medium",
        "priority": 7
    },
    {
        "path": "03-functions/medium/01_memoization_1.py",
        "title": "Memoization/Caching",
        "difficulty": "Medium",
        "priority": 8
    },
    {
        "path": "09-recursion/medium/01_fibonacci_1.py",
        "title": "Fibonacci Sequence",
        "difficulty": "Medium",
        "priority": 9
    },
    {
        "path": "10-oop/medium/01_design_class_1.py",
        "title": "Design a Stack Class",
        "difficulty": "Medium",
        "priority": 10
    },
    {
        "path": "11-dsa/medium/01_merge_intervals_1.py",
        "title": "Merge Intervals",
        "difficulty": "Medium",
        "priority": 11
    },
    {
        "path": "08-sorting-algorithms/medium/01_quicksort_1.py",
        "title": "Quick Sort Implementation",
        "difficulty": "Medium",
        "priority": 12
    },
    {
        "path": "04-data-structures/medium/01_lru_cache_1.py",
        "title": "LRU Cache",
        "difficulty": "Medium",
        "priority": 13
    },
    {
        "path": "07-arrays/hard/01_trapping_rain_water_1.py",
        "title": "Trapping Rain Water",
        "difficulty": "Hard",
        "priority": 14
    },
    {
        "path": "05-strings/hard/01_word_ladder_1.py",
        "title": "Word Ladder",
        "difficulty": "Hard",
        "priority": 15
    },
    {
        "path": "12-real-world-python/easy/01_file_parser_1.py",
        "title": "Parse CSV File",
        "difficulty": "Easy",
        "priority": 16
    },
    {
        "path": "12-real-world-python/medium/01_api_rate_limiter_1.py",
        "title": "API Rate Limiter",
        "difficulty": "Medium",
        "priority": 17
    },
    {
        "path": "13-python-for-ml-engineers/easy/01_data_preprocessing_1.py",
        "title": "Data Preprocessing",
        "difficulty": "Easy",
        "priority": 18
    },
    {
        "path": "13-python-for-ml-engineers/medium/01_train_test_split_1.py",
        "title": "Train/Test Split",
        "difficulty": "Medium",
        "priority": 19
    },
    {
        "path": "01-python-basics/medium/01_list_comprehension_1.py",
        "title": "List Comprehension",
        "difficulty": "Medium",
        "priority": 20
    }
]

print("="*70)
print("SHOWCASE PROBLEMS TO CREATE")
print("="*70)
print("\n✨ These 20 problems will transform the repository quality\n")

for i, problem in enumerate(SHOWCASE_PROBLEMS, 1):
    status = "✓" if i == 1 else " "  # First one (sort array) is done
    print(f"[{status}] {i:2d}. {problem['title']:40s} ({problem['difficulty']})")

print("\n" + "="*70)
print("NEXT STEPS:")
print("="*70)
print("\n1. Create each problem file with complete solution")
print("2. Test all solutions thoroughly")
print("3. Add to README as 'Featured Problems'")
print("4. Create GitHub issues for remaining problems")
print("\n" + "="*70)
