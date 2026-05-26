# LeetCode Solutions in Python

A personal collection of LeetCode problem solutions, all written in Python. This repository serves as a reference for revisiting problems, tracking progress, and practicing algorithmic thinking over time.

---

## What This Repository Contains

Each file in this folder is a standalone Python script that solves a specific LeetCode problem. The solutions cover a range of topics including arrays, strings, math, linked lists, sliding windows, dynamic programming, and bit manipulation. Problems span from easy to hard difficulty.

Every solution file includes:

- A `Solution` class with the method signature matching the LeetCode problem.
- A short test section at the bottom of the file that instantiates the class and runs a sample input, so you can verify the solution locally by simply running the file.
- Some files include commented-out alternative approaches or optimized versions alongside the primary solution.

There are currently **60 solutions** in this repository.

---

## File Naming Convention

Almost all files follow this naming pattern:

```
<problem-number>-<problem-name>.py
```

- **Problem number**: A four-digit, zero-padded number matching the LeetCode problem ID (e.g., `0001`, `0029`, `3740`).
- **Problem name**: A lowercase, hyphen-separated version of the problem title (e.g., `two-sum`, `divide-two-integers`, `sliding-window-maximum`).

### Examples

| Filename                                      | LeetCode Problem                                |
|-----------------------------------------------|--------------------------------------------------|
| `0001-two-sum.py`                             | #1 - Two Sum                                     |
| `0015-3sum.py`                                | #15 - 3Sum                                       |
| `0050-pow(x,n).py`                            | #50 - Pow(x, n)                                  |
| `0118-pascal's-triangle.py`                   | #118 - Pascal's Triangle                         |
| `0239-sliding-window-maximum.py`              | #239 - Sliding Window Maximum                    |
| `3740-minimum-distance-between-three-equal-elements-I.py` | #3740 - Minimum Distance Between Three Equal Elements I |

### Naming Exceptions

A couple of files deviate from the standard pattern:

- `Q8.py` -- An earlier solution for problem #8 (String to Integer), before the naming convention was adopted. The same problem also exists as `0008-string-to-integer.py` under the standard naming.
- `Q258.py` -- An earlier solution for problem #258, before the naming convention was adopted. The same problem also exists as `0258-addDigits.py` under the standard naming.
- `0258-addDigits.py` -- Uses camelCase instead of hyphen-separated words. Most files use lowercase hyphens, but a few like this one use camelCase from the original LeetCode method name.

---

## How Each Solution Is Structured

Every file is self-contained. You do not need to install anything beyond standard Python to run most of them. A typical file looks like this:

```python
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # solution logic here
        ...

c = Solution()
print(c.twoSum([2, 7, 11, 15], 9))
```

Key things to note:

1. **Class-based layout**: Solutions use the `class Solution` format that LeetCode expects. This makes it easy to copy-paste between this repository and the LeetCode editor.
2. **Runnable test at the bottom**: Each file ends with a quick instantiation and a print statement using sample inputs. You can run any file directly with `python <filename>` to see the output.
3. **Type hints**: Most solutions use Python type hints (`List[int]`, `Optional[...]`, etc.) consistent with LeetCode's provided signatures.
4. **Commented alternatives**: Several files contain commented-out blocks showing different approaches to the same problem -- for example, a brute-force version alongside an optimized one, or a mathematical solution next to an iterative one.

---

## How to Run a Solution

Pick any file and run it directly:

```bash
python 0001-two-sum.py
```

The script will print the result of the sample test case embedded at the bottom of the file. To test with different inputs, open the file and change the values passed to the method in the `print(...)` line.

---

## Dependencies

The vast majority of solutions use only Python's standard library. A few files import external packages:

- `numpy` -- Used in `3740-minimum-distance-between-three-equal-elements-I.py`
- `pandas` -- Imported (but commented out) in `0136-single-number.py`

Standard library modules used across various solutions include `typing`, `collections`, `itertools`, and `math`.

---

## Topics Covered

The problems in this collection span a wide range of categories:

| Category               | Example Problems                                           |
|------------------------|------------------------------------------------------------|
| Arrays and Hashing     | Two Sum, 3Sum, Remove Element, Single Number               |
| Strings                | Longest Substring, Zigzag Conversion, Valid Palindrome     |
| Math and Number Theory | Reverse Integer, Palindrome Number, Power of Three, Sqrt(x)|
| Linked Lists           | Add Two Numbers, Merge Two Sorted Lists                    |
| Two Pointers           | Container With Most Water, Reverse String, Reverse Vowels  |
| Sliding Window         | Sliding Window Maximum, Longest Substring Without Repeating|
| Binary Search          | Search Insert Position, Sqrt(x)                            |
| Dynamic Programming    | Climbing Stairs                                            |
| Bit Manipulation       | Single Number, XOR After Range Multiplication Queries      |
| Matrix                 | Rotate Image                                               |
| Simulation             | Walking Robot Simulation                                   |
| Stack                  | Valid Parentheses                                           |

---

## Full Problem Index

Below is the complete list of solved problems, ordered by problem number.

| #    | Problem Name                                      | Filename                                                    |
|------|---------------------------------------------------|-------------------------------------------------------------|
| 1    | Two Sum                                           | `0001-two-sum.py`                                           |
| 2    | Add Two Numbers                                   | `0002-add-two-numbers.py`                                   |
| 3    | Longest Substring Without Repeating Characters    | `0003-longest-substring.py`                                 |
| 4    | Median of Two Sorted Arrays                       | `0004-median-of-two-sorted-arrays.py`                       |
| 5    | Longest Palindromic Substring                     | `0005-longest-palindrome-substring.py`                      |
| 6    | Zigzag Conversion                                 | `0006-zigzag-conversion.py`                                 |
| 7    | Reverse Integer                                   | `0007-reverse-integer.py`                                   |
| 8    | String to Integer (atoi)                          | `0008-string-to-integer.py`                                 |
| 9    | Palindrome Number                                 | `0009-palindrome-number.py`                                 |
| 11   | Container With Most Water                         | `0011-container-with-most-water.py`                         |
| 12   | Integer to Roman                                  | `0012-integer-to-roman.py`                                  |
| 13   | Roman to Integer                                  | `0013-roman-to-integer.py`                                  |
| 14   | Longest Common Prefix                             | `0014-longest-common-prefix.py`                             |
| 15   | 3Sum                                              | `0015-3sum.py`                                              |
| 19   | Letter Combinations of a Phone Number             | `0019-letter-combinations-of-phone-number.py`               |
| 20   | Valid Parentheses                                  | `0020-valid-parentheses.py`                                 |
| 21   | Merge Two Sorted Lists                            | `0021-merge-two-sorted-lists.py`                            |
| 27   | Remove Element                                    | `0027-remove-element.py`                                    |
| 28   | Find the Index of the First Occurrence in a String| `0028-index-of-first-occurrence.py`                         |
| 29   | Divide Two Integers                               | `0029-divide-two-integers.py`                               |
| 35   | Search Insert Position                            | `0035-search-insert-position.py`                            |
| 38   | Count and Say                                     | `0038-count-and-say.py`                                     |
| 41   | First Missing Positive                            | `0041-first-missing-positive-number.py`                     |
| 43   | Multiply Strings                                  | `0043-multiply-strings.py`                                  |
| 48   | Rotate Image                                      | `0048-rotate-image.py`                                      |
| 50   | Pow(x, n)                                         | `0050-pow(x,n).py`                                          |
| 58   | Length of Last Word                                | `0058-length-of-last-word.py`                               |
| 66   | Plus One                                          | `0066-plus-one.py`                                          |
| 67   | Add Binary                                        | `0067-add-binary.py`                                        |
| 69   | Sqrt(x)                                           | `0069-sqrt(x).py`                                           |
| 70   | Climbing Stairs                                   | `0070-climbing-stairs.py`                                   |
| 88   | Merge Sorted Array                                | `0088-merge-sorted-arrays.py`                               |
| 118  | Pascal's Triangle                                 | `0118-pascal's-triangle.py`                                 |
| 119  | Pascal's Triangle II                              | `0119-pascal's-triangle-2.py`                               |
| 125  | Valid Palindrome                                  | `0125-valid-palindrome.py`                                  |
| 136  | Single Number                                     | `0136-single-number.py`                                     |
| 168  | Excel Sheet Column Title                          | `0168-excel-sheet-column-title.py`                          |
| 239  | Sliding Window Maximum                            | `0239-sliding-window-maximum.py`                            |
| 258  | Add Digits                                        | `0258-addDigits.py`                                         |
| 290  | Word Pattern                                      | `0290-word-pattern.py`                                      |
| 326  | Power of Three                                    | `0326-power-of-three.py`                                    |
| 344  | Reverse String                                    | `0344-reverse-string.py`                                    |
| 345  | Reverse Vowels of a String                        | `0345-reverse-vowels-of-string.py`                          |
| 415  | Add Strings                                       | `0415-add-strings.py`                                       |
| 520  | Detect Capital                                    | `0520-detect-capital.py`                                    |
| 541  | Reverse String II                                 | `0541-reverse-string-II.py`                                 |
| 657  | Robot Return to Origin                            | `0657-robot-return-to-origin.py`                            |
| 874  | Walking Robot Simulation                          | `0874-walking-robot-simulation.py`                          |
| 1848 | Minimum Distance to the Target Element            | `1848-minimum-distance-to-the-target-element.py`            |
| 1855 | Maximum Distance Between a Pair of Values         | `1855-maximum-distance-between-a-pair-of-values.py`         |
| 1980 | Find Unique Binary String                         | `1980-find-unique-binary-string.py`                         |
| 2078 | Two Furthest Houses With Different Colors         | `2078-two-furthest-houses-with-different-colors.py`         |
| 2452 | Words Within Two Edits of Dictionary              | `2452-words-within-two-edits-of-dictionary.py`              |
| 2515 | Shortest Distance to Target String in Circular Array | `2515-shortest-distance-to-target-string-in-circular-array.py` |
| 2615 | Sum of Distances                                  | `2615-sum-of-distances.py`                                  |
| 3120 | Count the number of Special Characters I                        | `3120-count-the-number-of-special-characters-I.py`                        |
| 2833 | Furthest Point From Origin                        | `2833-furthest-point-from-origin.py`                        |
| 3488 | Closest Equal Element Queries                     | `3488-closest-equal-element-queries.py`                     |
| 3653 | XOR After Range Multiplication Queries I          | `3653-xor-after-range-multiplication-queries-I.py`          |
| 3740 | Minimum Distance Between Three Equal Elements I   | `3740-minimum-distance-between-three-equal-elements-I.py`   |
| 3761 | Minimum Absolute Distance Between Mirror Pairs    | `3761-minimum-absolute-distance-between-mirror-pairs.py`    |
| 3783 | Mirror Distance of an Integer                     | `3783-mirror-distance-of-an-integer.py`                     |
| 3918 | Sum of Primes between Number and its Reverse                        | `3918-sum-of-primes-between-number-and-its-reverse.py`                        |
| 3921 | Score Validator                        | `3921-score-validator.py`                        |

Older duplicates also exist: `Q8.py` (same as problem #8, String to Integer) and `Q258.py` (same as problem #258, Add Digits).

---

## Notes

- This is a living repository. New solutions get added as problems are solved.
- Some solutions prioritize readability over optimal time complexity. Where an optimized version exists, it is usually included as a commented-out block within the same file.
- The numbering gap between files (e.g., jumping from `0015` to `0019`) simply means those problems have not been solved yet, not that anything is missing.
