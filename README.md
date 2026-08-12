# 🐍 Python Problem-Solving Roadmap

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![Problems](https://img.shields.io/badge/problems-843-brightgreen.svg)](https://github.com/yourusername/python-problem-solving)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

> A comprehensive collection of **843 Python problems** spanning from absolute basics to ML engineering, designed for structured learning and interview preparation.

---

## 📖 Table of Contents

- [Overview](#-overview)
- [Repository Structure](#-repository-structure)
- [Learning Paths](#-learning-paths)
- [Quick Start](#-quick-start)
- [Topics Covered](#-topics-covered)
- [Problem Format](#-problem-format)
- [How to Use](#-how-to-use)
- [Progress Tracking](#-progress-tracking)
- [Contributing](#-contributing)
- [Community](#-community)
- [License](#-license)

---

## 🎯 Overview

This repository is your complete guide to mastering Python through **structured problem-solving**. Whether you're:
- 🎓 A student learning Python fundamentals
- 💼 Preparing for technical interviews
- 🚀 Transitioning to ML/Data Science roles
- 📚 Teaching Python to others

You'll find **843 carefully crafted problems** with multiple difficulty levels across 13 comprehensive topics.

### ✨ What Makes This Different?

- **Progressive Difficulty**: Each topic has Easy → Medium → Hard problems
- **Complete Structure**: Every problem includes constraints, examples, hints, and test cases
- **Real-World Focus**: 20+ projects demonstrating practical applications
- **Interview Ready**: Problems tagged with common patterns (#two-pointers, #dynamic-programming, etc.)
- **ML Engineering Path**: Dedicated track for transitioning to ML roles

---

## 📂 Repository Structure

```
python-problem-solving/
├── 01-python-basics/          # 60 problems - Variables, data types, operators
├── 02-control-flow/           # 60 problems - Loops, conditionals, branching
├── 03-functions/              # 60 problems - Functions, recursion, decorators
├── 04-data-structures/        # 90 problems - Lists, dicts, sets, stacks, queues
├── 05-strings/                # 90 problems - String manipulation, parsing
├── 06-numbers/                # 60 problems - Math operations, algorithms
├── 07-arrays/                 # 90 problems - Array algorithms, sorting, searching
├── 08-sorting-algorithms/     # 60 problems - Sorting algorithm implementations
├── 09-recursion/              # 60 problems - Recursive problem solving
├── 10-oop/                    # 60 problems - Object-oriented programming
├── 11-dsa/                    # 90 problems - Advanced DSA, graphs, trees
├── 12-real-world-python/      # 20+ projects - Practical applications
└── 13-python-for-ml-engineers/ # 60 problems - NumPy, Pandas, sklearn, ML ops
```

**Total: 843 Problems + 20 Real-World Projects**

---

## 🗺️ Learning Paths

### Path 1: Complete Beginner (8-12 weeks)
```
Week 1-2:  01-python-basics (Easy)
Week 3-4:  02-control-flow (Easy → Medium)
Week 5-6:  03-functions (Easy → Medium)
Week 7-8:  04-data-structures (Easy)
Week 9-10: 05-strings (Easy) + 12-real-world-python (Beginner projects)
Week 11-12: Review and build personal project
```

### Path 2: Interview Preparation (4-6 weeks)
```
Week 1:   07-arrays (All) + 08-sorting-algorithms (Medium)
Week 2:   04-data-structures (Medium → Hard)
Week 3:   09-recursion (All) + 11-dsa (Easy → Medium)
Week 4:   11-dsa (Hard) - Focus on graphs, DP, trees
Week 5-6: Mock interviews + 12-real-world-python (Advanced projects)
```

### Path 3: ML Engineer Track (6-8 weeks)
```
Week 1-2: 01-python-basics (All) + 03-functions (Medium → Hard)
Week 3-4: 04-data-structures (All) + 10-oop (Medium)
Week 5-6: 13-python-for-ml-engineers (Easy → Medium)
Week 7-8: 13-python-for-ml-engineers (Hard) + Real ML projects
```

### Path 4: Quick Brush-Up (1-2 weeks)
Focus on Medium and Hard problems in topics 02, 03, 04, 07, 11

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Basic understanding of programming (for beginners, start with 01-python-basics)

### Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/python-problem-solving.git
cd python-problem-solving

# (Optional) Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# No dependencies required for basic problems
# For ML problems (Topic 13), install requirements
pip install -r requirements.txt
```

### Running Your First Problem

```bash
# Navigate to any problem
cd 01-python-basics/easy

# Open and solve
python 01_var_assignment.py

# Run tests
python 01_var_assignment.py
```

---

## 📚 Topics Covered

| # | Topic | Problems | Difficulty Split | Focus Areas |
|---|-------|----------|------------------|-------------|
| 01 | **Python Basics** | 60 | 20/20/20 | Variables, types, operators, syntax |
| 02 | **Control Flow** | 60 | 20/20/20 | Loops, conditionals, flow control |
| 03 | **Functions** | 60 | 20/20/20 | Functions, recursion, decorators, closures |
| 04 | **Data Structures** | 90 | 30/30/30 | Lists, dicts, sets, stacks, queues, trees |
| 05 | **Strings** | 90 | 30/30/30 | Manipulation, parsing, regex, formatting |
| 06 | **Numbers** | 60 | 20/20/20 | Math, primes, number theory |
| 07 | **Arrays** | 90 | 30/30/30 | Array algorithms, two pointers, sliding window |
| 08 | **Sorting** | 60 | 20/20/20 | All major sorting algorithms |
| 09 | **Recursion** | 60 | 20/20/20 | Recursive thinking, backtracking |
| 10 | **OOP** | 60 | 20/20/20 | Classes, inheritance, design patterns |
| 11 | **DSA** | 90 | 30/30/30 | Graphs, trees, DP, greedy, advanced algorithms |
| 12 | **Real-World** | 20+ | Projects | CLI apps, APIs, web scrapers, data pipelines |
| 13 | **ML Engineering** | 60 | 20/20/20 | NumPy, Pandas, sklearn, model deployment |

**Total**: 843 problems across 13 topics

---

## 📝 Problem Format

Each problem follows a consistent, educational format:

```python
"""
Problem: [Descriptive Title]
Difficulty: Easy/Medium/Hard
Tags: #relevant #tags #for #searching

Description
-----------
Clear problem statement with context and requirements

Constraints
-----------
- Input size limits
- Time complexity expectations
- Space complexity expectations

Examples
--------
Multiple examples including edge cases with explanations

Approach
--------
Step-by-step approach to solve the problem

Hints
-----
Progressive hints (try solving before reading!)

Solution
--------
"""

def solve():
    # Your solution here
    pass

# Test cases included
# Comprehensive documentation
# Common mistakes highlighted
```

---

## 💡 How to Use

### For Self-Study

1. **Choose your learning path** (see [Learning Paths](#-learning-paths))
2. **Start with Easy problems** in your first topic
3. **Try solving without hints** (20-30 min for Easy, 30-45 min for Medium)
4. **Read hints progressively** if stuck
5. **Compare your solution** with provided approaches
6. **Move to next difficulty** after completing 80% of current level

### For Interview Prep

1. **Focus on topics 04, 07, 09, 11** (data structures, arrays, recursion, DSA)
2. **Practice Medium and Hard problems** (simulate interview difficulty)
3. **Time yourself** (30-45 min per problem)
4. **Implement multiple approaches** (brute force → optimized)
5. **Explain your solution out loud** (practice communication)

### For Teaching

1. Use **Easy problems** for class demonstrations
2. **Medium problems** for homework/assignments
3. **Hard problems** for advanced students/bonus
4. **Real-world projects** for capstone/portfolio pieces

---

## 📊 Progress Tracking

### Method 1: Manual Checklist

Create your own progress tracker:
```markdown
## My Progress

### 01-python-basics
- [x] Easy: 01-10 ✓
- [ ] Easy: 11-20
- [ ] Medium: 01-20
- [ ] Hard: 01-20

### 02-control-flow
- [ ] Easy: 01-20
...
```

### Method 2: Git Branches

```bash
# Create your solution branch
git checkout -b my-solutions

# Track your progress
git add solved-problems/
git commit -m "Solved: arrays/medium/01-15"
```

### Method 3: Progress Script (Coming Soon)

We're building an interactive progress tracker. Star the repo to get notified!

---

## 🤝 Contributing

We welcome contributions! Here's how you can help:

### Ways to Contribute

1. **Add Solutions**: Share your unique approaches
2. **Improve Problem Statements**: Make descriptions clearer
3. **Add Test Cases**: More edge cases = better learning
4. **Create Projects**: Add real-world applications
5. **Fix Bugs**: Spot an error? Submit a PR
6. **Improve Documentation**: Help others learn better

### Contribution Guidelines

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Follow existing code style and format
4. Add tests for new problems
5. Update documentation if needed
6. Commit your changes (`git commit -m 'Add: Amazing new problem'`)
7. Push to the branch (`git push origin feature/AmazingFeature`)
8. Open a Pull Request

See [CONTRIBUTING.md](CONTRIBUTING.md) for detailed guidelines.

---

## 🌟 Community

- **Issues**: Report bugs or request features via [GitHub Issues](https://github.com/yourusername/python-problem-solving/issues)
- **Discussions**: Ask questions, share solutions in [Discussions](https://github.com/yourusername/python-problem-solving/discussions)
- **Star the repo**: Show your support ⭐
- **Share**: Help others discover this resource

### Success Stories

Share your journey! Tag us with `#PythonProblemSolving` on Twitter/LinkedIn.

---

## 📈 Roadmap

### Coming Soon

- [ ] Interactive web interface for progress tracking
- [ ] Video explanations for Hard problems
- [ ] Community solution submissions
- [ ] Monthly coding challenges
- [ ] Discord server for live help
- [ ] Mobile-friendly problem viewer

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

You are free to:
- ✓ Use for personal learning
- ✓ Use for teaching
- ✓ Modify and distribute
- ✓ Use commercially

---

## 🙏 Acknowledgments

- Inspired by LeetCode, HackerRank, and ProjectEuler
- Built for the Python learning community
- Special thanks to all contributors

---

## 📬 Contact

- **GitHub**: [@yourusername](https://github.com/yourusername)
- **Email**: your.email@example.com
- **Twitter**: [@yourhandle](https://twitter.com/yourhandle)

---

<div align="center">

### ⭐ Star this repository if you find it helpful!

**Happy Coding! 🚀**

Made with ❤️ for the Python community

</div>
