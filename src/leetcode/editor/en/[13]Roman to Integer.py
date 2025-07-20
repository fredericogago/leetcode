"""🔢 LeetCode Problem: 13 - Roman to Integer - https://leetcode.com/problems/roman-to-integer/

🧩 Description:
Converts a string representing a Roman numeral into its corresponding integer value.
Roman numerals are written from largest to smallest from left to right,
except in six specific cases where a smaller value precedes a larger one
to indicate subtraction (e.g., IV = 4, CM = 900).

📌 Symbol table:
    Symbol       Value
    I             1
    V             5
    X             10
    L             50
    C             100
    D             500
    M             1000

👨‍💻 Explored Approaches:

✅ 1. Idiomatic version (simple and efficient)
    - Uses a single loop with the condition `value > prev_value` to detect
        subtraction
    - Performs calculation inline with:
        `total += value - 2 * prev_value if value > prev else value`
    - 🟢 Best for performance, readability, and interview settings.
    - ✅ Runtime: 3 ms (faster than 79.17% of Python3 submissions).
    - ✅ Memory Usage: 17.6 MB (less than 90.19% of Python3 submissions).

🔁 2. Functional/Overengineered version with operators
    - Uses `operator.add` and `operator.sub` instead of raw `+` and `-`
    - Builds a list of `(value, operator)` pairs, or alternatively
        yields incremental totals
    - ⚠️ Slower (~30% overhead), but useful for teaching, debugging,
        or step-by-step tracing

📊 Benchmarks (input: `"MCMXCIV" * 1000`):

| Version                  | Avg. time (100K runs)  | Notes                            |
|--------------------------|------------------------|----------------------------------|
| Idiomatic version        | ~145 ms                | Fastest and cleanest             |
| Overengineered (list)    | ~205 ms                | Uses intermediate list of ops    |
| Overengineered (yield)   | ~195 ms                | Uses generator for step-by-step  |

🧮 Complexity Analysis:

Time Complexity:
    - Best case: O(n)
    - Worst case: O(n)
    - Average case: O(n)
    where n is the length of the input Roman numeral string (at most 15).

Space Complexity:
    - Idiomatic version: O(1)
        - Constant space for total and prev_value.
        - SYMBOLS is static and does not grow with input.
    - Overengineered (list): O(n)
        - Stores a list of operations (value, operator) pairs.
    - Overengineered (generator): O(1)
        - No persistent structure; yields values on-the-fly.
        - Slightly higher call stack overhead from the generator.

Note: All versions run in linear time due to the one-pass traversal
over the input string, but differ in memory usage due to intermediate
constructs.

⏱️ Time invested:
    - Reading and understanding the problem: 20 minutes
    - Coding, refactoring, and analyzing with ChatGPT: 50 minutes
    - 🔄 Total: **1h10min**

🧠 Challenges encountered:
    - Initially didn’t realize that `value > prev_value` elegantly captures
        all valid subtractive combinations
    - Tried building a list of operations with `operator` before understanding
        the performance/clarity tradeoff
    - Learned that even with `operator`, one can avoid intermediate lists and
        use `yield` incrementally

💡 Technical note:
Even when pursuing a deliberately overengineered approach, it's possible to
retain clarity and improve performance by eliminating unnecessary data
structures and applying inline logic functionally.

✍️ Personal note:
This exercise turned a seemingly trivial problem into a great opportunity
to explore symbolic parsing, performance benchmarking, and clean software
design in Python.

🏷️ Tags:
#Python #LeetCode #CleanCode #Performance #ProblemSolving #Refactor
#FunctionalProgramming #DeveloperJourney
"""

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D
# and M. 
# 
#  
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000 
# 
#  For example, 2 is written as II in Roman numeral, just two ones added 
# together. 12 is written as XII, which is simply X + II. The number 27 is written as 
# XXVII, which is XX + V + II. 
# 
#  Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is written as 
# IV. Because the one is before the five we subtract it making four. The same 
# principle applies to the number nine, which is written as IX. There are six 
# instances where subtraction is used: 
# 
#  
#  I can be placed before V (5) and X (10) to make 4 and 9. 
#  X can be placed before L (50) and C (100) to make 40 and 90. 
#  C can be placed before D (500) and M (1000) to make 400 and 900. 
#  
# 
#  Given a roman numeral, convert it to an integer. 
# 
#  
#  Example 1: 
# 
#  
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
#  
# 
#  Example 2: 
# 
#  
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
#  
# 
#  Example 3: 
# 
#  
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 15 
#  s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M'). 
#  It is guaranteed that s is a valid roman numeral in the range [1, 3999]. 
#  
# 
#  Related Topics Hash Table Math String 👍 16164 👎 1114
# leetcode submit region begin(Prohibit modification and deletion)
from typing import ClassVar

class Solution:
    """LeetCode Problem: Roman to Integer

    https://leetcode.com/problems/roman-to-integer/

    Converts a Roman numeral to its integer representation using a single-pass
    approach. The algorithm adds each symbol's value unless a smaller value
    precedes a larger one, in which case it applies a subtractive correction.

    Attributes:
        SYMBOLS (ClassVar[dict[str, int]]): A mapping of Roman numeral symbols
            to their integer values.
    """

    SYMBOLS: ClassVar[dict[str, int]] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        """Converts a Roman numeral string to an integer.

        The method iterates through the string from left to right, applying
        a subtractive rule when a symbol with a larger value follows a smaller
        one.

        Args:
            s (str): A string containing a valid Roman numeral
                (e.g., "MCMXCIV").

        Returns:
            int: The integer representation of the Roman numeral.
        """
        total = 0
        prev_value = 0

        for c in s:
            value = self.SYMBOLS[c]
            # If the current value is greater than the previous one,
            # we need to subtract twice the previous value
            # (because it was added before).
            total += value - 2 * prev_value if value > prev_value else value
            prev_value = value
        return total


# leetcode submit region end(Prohibit modification and deletion)

from collections.abc import Generator
from collections.abc import Callable

from typing import ClassVar
import operator

class SolutionOverEngineer:
    """LeetCode Problem: Roman to Integer

    https://leetcode.com/problems/roman-to-integer/

    Converts a Roman numeral to its integer representation using symbolic
    parsing with functional operators and a generator for step-by-step
    evaluation. This approach is more flexible and educational but
    less performant.

    Attributes:
        SYMBOLS (ClassVar[dict[str, int]]): A mapping of Roman numeral symbols
            to their integer values.
    """

    SYMBOLS: ClassVar[dict[str, int]] = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    def romanToInt(self, s: str) -> int:
        """Converts a Roman numeral string to an integer.

        This method uses a generator (`romanToGenerator`) that yields the
        accumulated total at each step, applying either addition or a
        subtractive correction based on symbol order.

        Args:
            s (str): A string containing a valid Roman numeral
                (e.g., "MCMXCIV").

        Returns:
            int: The final integer value after applying all
                operator-based steps.
        """
        return sum(self.romanToGenerator(s))

    def romanToGenerator(self, s: str) -> Generator[int, None, None]:
        """Generates intermediate totals from a Roman numeral string.

        At each step, decides whether to apply addition or subtraction 
        based on the relative order of the current and previous symbols.
        Uses the `operator` module for functional dispatch.

        Args:
            s (str): A Roman numeral string.

        Yields:
            int: The running total after processing each character.
        """
        prev_val = 0
        total = 0

        for c in s:
            curr_val = self.SYMBOLS[c]
            op: Callable[[int, int], int] = (
                operator.sub if prev_val < curr_val else operator.add
            )
            delta = curr_val if op is operator.add else curr_val - 2 * prev_val
            total += delta
            yield total
            prev_val = curr_val
