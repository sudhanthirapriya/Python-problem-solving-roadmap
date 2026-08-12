# 🚀 Getting Started Guide

Welcome! This guide will help you start solving problems in under 5 minutes.

## 📋 Prerequisites

- **Python 3.8+** installed ([Download Python](https://www.python.org/downloads/))
- **Text Editor or IDE** (VS Code, PyCharm, Sublime, or any editor)
- **Terminal/Command Prompt** access
- **Basic Python knowledge** (if complete beginner, start with Topic 01)

## ⚡ Quick Start (5 Minutes)

### Step 1: Get the Code

**Option A: Clone with Git** (Recommended)
```bash
git clone https://github.com/yourusername/python-problem-solving.git
cd python-problem-solving
```

**Option B: Download ZIP**
1. Click green "Code" button on GitHub
2. Select "Download ZIP"
3. Extract to your preferred location
4. Open terminal in that folder

### Step 2: Verify Python

```bash
# Check Python version (should be 3.8+)
python --version
# or
python3 --version
```

If Python is not installed, download from [python.org](https://www.python.org/downloads/).

### Step 3: Solve Your First Problem!

```bash
# Navigate to first problem
cd 01-python-basics/easy

# Open the first problem
python 01_var_assignment.py
```

You should see output! Now open `01_var_assignment.py` in your editor and start solving.

## 📖 Understanding Problem Structure

Each problem file contains:

```python
"""
Problem: [Title]              # What you need to solve
Difficulty: Easy              # Easy/Medium/Hard
Tags: #relevant #tags         # For searching similar problems

Description                   # Detailed explanation
-----------
[Problem statement]

Constraints                   # Limits and requirements
-----------
[Input/output constraints]

Examples                      # Test your understanding
--------
[Multiple examples with explanations]

Approach                      # How to think about it
--------
[Step-by-step approach]

Hints                         # Progressive help
-----
[Try these if stuck]
"""

def solve():                  # ← YOUR CODE GOES HERE
    # TODO: Implement solution
    pass

# Test cases at bottom        # Verify your solution works
```

## 🎯 How to Solve Problems

### Method 1: Read → Think → Code → Test

1. **Read** the problem carefully (2-3 times)
2. **Understand** examples and constraints
3. **Think** about approach (use hints if stuck)
4. **Code** your solution in the `solve()` function
5. **Test** by running the file: `python filename.py`

### Method 2: Test-Driven Approach

1. Read the problem
2. Write test cases first
3. Implement solution
4. Run tests until all pass

### Example Workflow

```python
# 1. Read problem (in docstring)
# 2. Implement solution
def solve(numbers):
    """Find sum of all numbers"""
    total = 0
    for num in numbers:
        total += num
    return total

# 3. Add test cases
def test_solve():
    assert solve([1, 2, 3]) == 6
    assert solve([]) == 0
    assert solve([-1, 1]) == 0
    print("✓ All tests passed!")

# 4. Run
if __name__ == "__main__":
    test_solve()
```

## 🗺️ Recommended Learning Paths

### 🌱 Complete Beginner (Never coded before)

**Week 1-2: Python Basics**
```bash
cd 01-python-basics/easy
# Solve problems 01-20 in order
```

**Week 3-4: Control Flow**
```bash
cd 02-control-flow/easy
# Practice loops and conditions
```

**Week 5-6: Functions**
```bash
cd 03-functions/easy
# Learn function concepts
```

Continue with easy problems until comfortable, then move to medium.

### 💼 Interview Preparation (4-6 weeks)

Focus on these topics in order:

1. **Arrays** (07-arrays) - Most common in interviews
2. **Data Structures** (04-data-structures) - Essential knowledge
3. **Recursion** (09-recursion) - Important pattern
4. **DSA** (11-dsa) - Advanced algorithms

**Daily Schedule:**
- Solve 2-3 medium problems (45-60 min each)
- Review 1 hard problem solution
- Practice explaining your approach out loud

### 🤖 ML Engineer Track (6-8 weeks)

**Week 1-2: Python Foundations**
- 01-python-basics (all)
- 03-functions (medium + hard)

**Week 3-4: Data Structures**
- 04-data-structures (all)
- 10-oop (medium)

**Week 5-8: ML Specific**
- 13-python-for-ml-engineers (all)
- Focus on NumPy, Pandas, sklearn

## 🛠️ Setting Up Your Environment

### Option 1: Simple Setup (Recommended for Beginners)

Just Python + any text editor. No setup needed!

### Option 2: Virtual Environment (Recommended)

Keep dependencies isolated:

```bash
# Create virtual environment
python -m venv venv

# Activate it
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
source venv/bin/activate

# Install dependencies (only for ML problems)
pip install -r requirements.txt
```

### Option 3: Full IDE Setup

**VS Code:**
1. Install [VS Code](https://code.visualstudio.com/)
2. Install Python extension
3. Open folder: `File → Open Folder → python-problem-solving`
4. Select Python interpreter: `Ctrl+Shift+P` → "Python: Select Interpreter"

**PyCharm:**
1. Install [PyCharm](https://www.jetbrains.com/pycharm/)
2. Open project: `File → Open → python-problem-solving`
3. Configure Python interpreter in settings

## 📊 Tracking Your Progress

### Method 1: Create Progress File

Create `my-progress.md`:

```markdown
# My Progress

## Topic 01: Python Basics
- [x] Easy: 01-10 ✓ (Dec 15)
- [ ] Easy: 11-20
- [ ] Medium: 01-20
- [ ] Hard: 01-20

## Topic 02: Control Flow
- [ ] Easy: 01-20
...
```

### Method 2: Use Git Branches

```bash
# Create your personal branch
git checkout -b my-solutions

# Make commits as you solve
git add solved-problems/
git commit -m "Solved: arrays easy 01-05"
```

### Method 3: Simple Checklist

Keep a text file or spreadsheet with problem names and checkboxes.

## 💡 Tips for Success

### General Tips

1. **Be consistent**: 30 min/day better than 5 hours once a week
2. **Don't rush**: Understanding > Speed
3. **Use hints wisely**: Try 15-20 min before looking at hints
4. **Review solutions**: Even after solving, read provided solutions
5. **Track progress**: Motivation comes from seeing progress

### When Stuck

1. Read problem again carefully
2. Try smaller example on paper
3. Check Hint 1
4. Still stuck? Check Hint 2
5. Still stuck? Check Hint 3
6. Still stuck? Look at solution approach, then try again

### Time Management

- **Easy problems**: 15-25 minutes
- **Medium problems**: 25-45 minutes  
- **Hard problems**: 45-60 minutes

If stuck longer, it's OK to check the solution and learn!

## 🎓 Learning Resources

### Within This Repo

- Problem hints and approaches
- Test cases to understand requirements
- Related problems for practice

### External Resources

- **Python Docs**: [docs.python.org](https://docs.python.org)
- **Python Tutor**: [pythontutor.com](http://pythontutor.com) - Visualize code execution
- **Real Python**: [realpython.com](https://realpython.com) - Tutorials
- **Stack Overflow**: For specific questions

## ❓ Common Issues

### "python command not found"

Try `python3` instead of `python`:
```bash
python3 filename.py
```

### "Module not found" Error

Install requirements:
```bash
pip install -r requirements.txt
```

### "Permission Denied"

On Mac/Linux, you may need to make files executable:
```bash
chmod +x filename.py
```

### Tests Not Running

Make sure you're running from the problem directory:
```bash
cd 01-python-basics/easy
python 01_var_assignment.py
```

## 🤝 Getting Help

### When You Need Help

1. **Read documentation**: Problem description, hints, examples
2. **Search existing issues**: Someone may have asked already
3. **Ask in Discussions**: Share your approach, ask for guidance
4. **Open an issue**: If you think there's a bug

### How to Ask Good Questions

Include:
- Problem name and path
- What you tried
- Error message (if any)
- Your Python version

**Good question:**
> I'm working on 07-arrays/medium/05_sliding_window.py. I tried using two pointers but getting index out of range error on line 15. Here's my code: [code]. Python 3.9.

**Bad question:**
> It doesn't work. Help!

## 🎉 Next Steps

1. ✅ Pick your learning path
2. ✅ Navigate to first topic
3. ✅ Solve your first problem
4. ✅ Track your progress
5. ✅ Keep going!

---

**Remember**: Everyone starts somewhere. Don't compare your progress to others. Focus on consistent improvement! 🚀

**Happy Coding!** 

---

*Having trouble? Open an issue or ask in Discussions!*
