# Contributing to Python Problem-Solving Roadmap

First off, thank you for considering contributing to this project! 🎉

This document provides guidelines for contributing to the Python Problem-Solving Roadmap. Following these guidelines helps maintain quality and makes the contribution process smooth for everyone.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guide](#style-guide)
- [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)

---

## Code of Conduct

This project adheres to a Code of Conduct that all contributors are expected to follow:

- **Be respectful**: Treat everyone with respect and kindness
- **Be inclusive**: Welcome contributors from all backgrounds
- **Be collaborative**: Work together constructively
- **Be patient**: Remember everyone is learning

---

## How Can I Contribute?

### 🐛 Reporting Bugs

Found a bug? Help us fix it!

1. **Check existing issues** to avoid duplicates
2. **Create a new issue** with:
   - Clear, descriptive title
   - Steps to reproduce the bug
   - Expected vs actual behavior
   - Python version and OS
   - Code snippet if applicable

### 💡 Suggesting Enhancements

Have an idea? We'd love to hear it!

1. **Check existing issues** for similar suggestions
2. **Create a new issue** describing:
   - The problem you're trying to solve
   - Your proposed solution
   - Why this would be useful
   - Examples if applicable

### ✅ Contributing Code

#### Types of Contributions Welcome

1. **Add Solutions**: Implement solutions to existing problems
2. **Add Test Cases**: More comprehensive edge cases
3. **Improve Problem Statements**: Clearer descriptions, better examples
4. **Add New Problems**: Well-structured problems with complete format
5. **Create Projects**: Real-world applications in topic 12
6. **Fix Typos/Bugs**: Documentation or code corrections
7. **Improve Documentation**: Better explanations, tutorials, examples

---

## Contribution Guidelines

### Before You Start

1. **Fork the repository** to your GitHub account
2. **Clone your fork** locally
   ```bash
   git clone https://github.com/YOUR-USERNAME/python-problem-solving.git
   cd python-problem-solving
   ```
3. **Create a branch** for your changes
   ```bash
   git checkout -b feature/your-feature-name
   ```

### Adding Solutions

When adding a solution to an existing problem:

1. **Keep the existing structure**: Don't remove the problem format
2. **Implement the `solve()` function**: This is the main solution
3. **Add comments**: Explain your approach, not just what the code does
4. **Include complexity analysis**: Time and space complexity
5. **Add test cases**: At least 3-5 comprehensive test cases
6. **Consider multiple approaches**: Show brute force → optimized

**Example Solution Format:**

```python
def solve(input_data):
    """
    Brief description of approach.
    
    Approach:
    1. Step 1 explanation
    2. Step 2 explanation
    3. Step 3 explanation
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    
    Args:
        input_data: Description of input
        
    Returns:
        Description of return value
    """
    # Implementation with clear comments
    result = None
    
    # Step 1: Explain what this does
    # ...
    
    # Step 2: Explain next step
    # ...
    
    return result


# Test cases
def test_solve():
    # Test 1: Normal case
    assert solve(input1) == expected1, "Test case 1 failed"
    
    # Test 2: Edge case
    assert solve(input2) == expected2, "Test case 2 failed"
    
    # Test 3: Boundary condition
    assert solve(input3) == expected3, "Test case 3 failed"
    
    print("✓ All tests passed!")
```

### Adding New Problems

New problems should follow this structure:

```python
"""
Problem: [Clear, Descriptive Title]
Difficulty: Easy/Medium/Hard
Tags: #tag1 #tag2 #tag3 #tag4

Description
-----------
Clear problem statement (2-4 sentences)
Explain what needs to be done
Include real-world context if applicable

Constraints
-----------
- Input constraints (size, type, range)
- Time complexity expected
- Space complexity expected
- Special conditions

Examples
--------
Example 1:
Input: [clear input]
Output: [expected output]
Explanation: [why this output, step by step]

Example 2 (Edge Case):
Input: [edge case]
Output: [expected output]
Explanation: [handling edge case]

Example 3 (Another Case):
Input: [another scenario]
Output: [expected output]
Explanation: [reasoning]

Approach
--------
1. High-level approach step 1
2. High-level approach step 2
3. Key insight or algorithm to use
4. Edge cases to consider

Hints
-----
Hint 1: [Gentle nudge in right direction]
Hint 2: [Stronger hint]
Hint 3: [Almost gives away the solution]

Solution
--------
"""

def solve():
    """Solution implementation"""
    pass

"""
Common Mistakes
--------------
1. [Common mistake 1]
2. [Common mistake 2]
3. [Common mistake 3]

Edge Cases to Test
------------------
- [Edge case 1]
- [Edge case 2]
- [Edge case 3]

Related Problems
---------------
- [Related problem 1]
- [Related problem 2]

Practice Tips
-------------
- [Tip 1]
- [Tip 2]
"""
```

### Adding Projects

Projects in `12-real-world-python/` should:

1. **Solve a real problem**: Practical, useful application
2. **Include README**: Project description, setup, usage
3. **Have clear structure**: Well-organized code
4. **Include requirements**: Dependencies in requirements.txt
5. **Add tests**: Basic test coverage
6. **Document thoroughly**: Comments and docstrings

**Project Structure:**
```
12-real-world-python/
└── your-project-name/
    ├── README.md           # Project documentation
    ├── main.py            # Entry point
    ├── requirements.txt   # Dependencies
    ├── tests.py           # Test suite
    └── utils.py           # Helper functions (if needed)
```

---

## Style Guide

### Python Code Style

Follow PEP 8 with these specifics:

- **Indentation**: 4 spaces (no tabs)
- **Line length**: Max 88 characters (Black formatter standard)
- **Naming**:
  - `snake_case` for functions and variables
  - `PascalCase` for classes
  - `UPPER_CASE` for constants
- **Docstrings**: Use triple quotes for all functions
- **Comments**: Explain WHY, not WHAT
- **Imports**: Standard library → Third-party → Local

**Good:**
```python
def calculate_fibonacci(n: int) -> int:
    """
    Calculate the nth Fibonacci number.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        
    Returns:
        The nth Fibonacci number
    """
    if n <= 1:
        return n
    return calculate_fibonacci(n - 1) + calculate_fibonacci(n - 2)
```

**Bad:**
```python
def calc(n):
    # calculate fibonacci
    if n<=1:return n
    return calc(n-1)+calc(n-2)
```

### Documentation Style

- Use **Markdown** for all documentation
- Use **clear headings** and structure
- Include **code examples** where helpful
- Use **emoji sparingly** (only in README/guides)
- **No spelling errors**: Proofread your content

---

## Commit Message Guidelines

Write clear, descriptive commit messages:

### Format

```
<type>: <subject>

<body (optional)>

<footer (optional)>
```

### Types

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes (no code change)
- `refactor`: Code refactoring
- `test`: Adding tests
- `chore`: Maintenance tasks

### Examples

**Good:**
```
feat: Add solution for arrays/medium/sliding_window

Implemented optimized O(n) solution using sliding window technique.
Added comprehensive test cases covering edge cases.
```

**Good:**
```
fix: Correct time complexity in binary_search problem

Changed from O(log n) to O(n log n) to account for initial sorting step.
```

**Bad:**
```
update stuff
```

**Bad:**
```
fixed it
```

---

## Pull Request Process

### Before Submitting

1. ✅ **Test your code**: All tests pass
2. ✅ **Follow style guide**: Code is properly formatted
3. ✅ **Update documentation**: If adding features
4. ✅ **Check for conflicts**: Merge latest main branch
5. ✅ **Review your changes**: Read through your diff

### PR Title Format

Use the same format as commit messages:
```
<type>: <clear description>
```

Examples:
- `feat: Add BFS solution to graph traversal problem`
- `docs: Improve README quick start section`
- `fix: Correct edge case handling in merge_sort`

### PR Description Template

```markdown
## Description
[Clear description of what this PR does]

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Documentation update
- [ ] Code refactoring
- [ ] Test addition

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] All existing tests pass
- [ ] Added new tests for new functionality
- [ ] Manually tested changes

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-reviewed the code
- [ ] Commented complex sections
- [ ] Updated documentation if needed
- [ ] No new warnings generated
```

### Review Process

1. **Automated checks** will run (once set up)
2. **Maintainers will review** within 3-5 days
3. **Address feedback**: Make requested changes
4. **Approval & merge**: Once approved, we'll merge!

---

## Questions?

- **Open an issue**: For questions about contributing
- **Join discussions**: Share ideas and get feedback
- **Check existing issues**: Someone may have asked already

---

## Recognition

All contributors will be:
- Added to contributors list
- Credited in release notes
- Mentioned in acknowledgments

Thank you for helping make this resource better! 🙏

---

**Happy Contributing!** 🚀
