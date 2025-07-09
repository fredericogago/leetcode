"""
Module: palindrome_number

This module provides **three solutions** to check whether an integer is a
palindrome — that is, whether it reads the same forward and backward — **with
or without converting the number to a string**.

Problem:
--------
Given an integer `x`, return `True` if `x` is a palindrome, and `False` otherwise.

Constraints:
    -2³¹ <= x <= 2³¹ - 1

Examples:
    Input:  x = 121   → Output: True
    Input:  x = -121  → Output: False
    Input:  x = 10    → Output: False

Follow-up:
    Could you solve it **without converting the integer to a string**?

Solutions Implemented:
-----------------------
1. 🔤 `SolutionStr` – **String-based approach**
    - Converts the integer to a string and checks if the reversed string is
    equal to the original.
    - ✅ Simple and performant (Runtime: 4 ms, Beats 80.12%)
    - ❌ Does not fulfill the follow-up constraint

2. 🧮 `SolutionMath` – **Mathematical closed-form digit reversal**
    - Uses a formula based on powers of 10 and floor division:
        reverse(x) = x × 10ⁿ − 99 × Σₖ floor(x / 10ᵏ) × 10ⁿ⁻ᵏ
    - Inspired by: https://math.stackexchange.com/q/480068
    - ✅ Mathematically elegant
    - ⚠️ Slightly slower and sensitive to floating-point rounding
    - ✅ No strings used

3. 🔁 `Solution` – **Iterative digit reversal (preferred)**
    - Reverses the number using repeated division and modulus:
        while x > 0: result = result × 10 + x % 10
    - ✅ Fully arithmetic, fast, easy to debug
    - ✅ Best option for production
    - ✅ Satisfies the follow-up constraint

Benchmark Results:
-------------------
Tested on numbers with increasing digit counts (11, 101, 1001, ..., 10000001)

    Iterative Duration : ~0.000009 seconds
    Math Duration      : ~0.000033 seconds

Conclusion:
-----------
- Both non-string methods return correct results for all tested inputs.
- The **iterative solution is ~3.7× faster** than the mathematical one.
- Use `Solution` for performance-critical environments.
- `SolutionMath` is an interesting academic alternative.
- `SolutionStr` is fine for quick prototyping when constraints don’t matter.

Time Invested:
--------------
- Reading problem, analyzing constraints, diagramming logic: 20 minutes
- Coding, testing, refactoring, benchmarking: 1 hour 13 minutes

🕐 Total time: **1 hour 33 minutes**

Personal Note:
--------------
This exercise helped reinforce clean arithmetic logic, floating-point edge cases, and benchmarking practices.
It was a good opportunity to write and compare **clean, elegant Python 3.13 solutions** — and deepen my understanding of both performance and readability.

"""


# Given an integer x, return true if x is a palindrome, and false otherwise.
# 
#  
#  Example 1: 
# 
#  
# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
#  
# 
#  Example 2: 
# 
#  
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it 
# becomes 121-. Therefore it is not a palindrome.
#  
# 
#  Example 3: 
# 
#  
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
#  
# 
#  
#  Constraints: 
# 
#  
#  -2³¹ <= x <= 2³¹ - 1 
#  
# 
#  
# Follow up: Could you solve it without converting the integer to a string?
# 
#  Related Topics Math 👍 14207 👎 2826


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    """Check if an integer is a palindrome without converting to a string.

    This class provides a method to determine whether a given integer
    reads the same forward and backward, using only arithmetic operations.

    LeetCode Submission Stats:
        Runtime      : 31 ms, faster than 5.41% of Python3 online submissions
        Memory Usage : 17.7 MB, less than 64.13% of Python3 online submissions

    Complexity:
        Time Complexity:
            - O(log₁₀(n)) → We reverse the digits by repeatedly dividing by 10,
                which takes as many steps as the number of digits in n.
        Space Complexity:
            - O(1) → Constant extra space is used (no recursion, no data structures).
        Auxiliary Space:
            - O(1) → No call stack, no memory-intensive operations; just a few integers.
    """

    def isPalindrome(self, x: int) -> bool:
        """Check if a number is palindrome

        In a par:
            - To get the right half of the number as int we do:
                n // _determine_total_of_digits(n)
            - To get the left half of the number as int we do:
                n % _determine_total_of_digits(n)

        Args:
            x (int): The number to check if it is a palindrome

        Returns:
            bool: True if it is a palindrome, false otherwise.
        """
        if x < 0:
            return False
        return x == self._reverse_digits(x)

    @staticmethod
    def _reverse_digits(x: int) -> int:
        """
        Reverses the digits of a positive integer using arithmetic operations.

        Args:
            x (int): A non-negative integer.

        Returns:
            int: The integer formed by reversing the digits of x.

        Example:
            _reverse_digits(123)  → 321
            _reverse_digits(100)  → 1
            _reverse_digits(0)    → 0
        """
        result = 0
        while x > 0:
            result = result * 10 + x % 10  # shift digits left and add last digit
            x //= 10  # drop the last digit
        return result


# leetcode submit region end(Prohibit modification and deletion)
import math

class SolutionMath:
    """Palindrome check using mathematical digit reversal (no string conversion).

    This class solves the palindrome number problem by applying a
    closed-form digit reversal formula, derived from mathematical digit
    manipulation using base-10 logarithms and powers.

    It avoids string conversion completely, and uses:
        reverse(x) = x * 10^n - 99 * sum_{k=1}^{n} floor(x / 10^k) * 10^{n - k}
    with n = total digits - 1

    Complexity:
        Time Complexity:
            - O(log₁₀(n)) due to digit-based iteration (same as iterative method)
            - But includes costly math operations (log10, exponentiation)
        Space Complexity:
            - O(1) → Uses constant extra space
        Auxiliary Space:
            - O(1) → No recursion or containers, just scalar variables

    ⚠️ Warning:
        - This approach, while mathematically elegant, may be slightly
        slower in practice due to:
            - Floating-point rounding in log10
            - Expensive pow() operations
        - Prefer the iterative method (`Solution`) for runtime performance.
    """

    def isPalindrome(self, x: int) -> bool:
        """Check if a number is palindrome

        In a par:
            - To get the right half of the number as int we do:
                n // _determine_total_of_digits(n)
            - To get the left half of the number as int we do:
                n % _determine_total_of_digits(n)

        Args:
            x (int): The number to check if it is a palindrome

        Returns:
            bool: True if it is a palindrome, false otherwise.
        """
        if x < 0:
            return False
        return x == self._reverse_numbers(x)

    @staticmethod
    def _determine_total_of_digits(x: int) -> int:
        """Returns the number of digits in a positive integer using base-10.

        This works by computing the base-10 logarithm of the number, which
        gives the order of magnitude (i.e., how many times 10 must be
        multiplied to reach the number). The number of digits is then
        obtained by taking the integer part of log10(num) and adding 1.

        For example:
            log10(1221) ≈ 3.08 → int(3.08) + 1 = 4 digits
            log10(121)  ≈ 2.08 → int(2.08) + 1 = 3 digits

        Args:
            x (int): The integer to determine the total digits.

        Returns:
            int: The total digits.

        Raises:
            ValueError if x is not a positive integer.
        """
        if x < 0:
            raise ValueError("x must be non-negative")

        if x == 0:
            return 1

        return int(math.log10(x)) + 1

    @staticmethod
    def _reverse_numbers(x: int) -> int:
        """Reverses the digits of a positive integer.


        This function implements a closed-form expression based on:
            reverse(x) = x * 10^n - 99 * sum_{k=1}^{n} floor(x / 10^k) * 10^{n - k}

        where n = number of digits - 1

        Example:
            reverse_number(123) => 321
            reverse_number(100) => 1  (leading zeros are discarded)
            reverse_number(1200) => 21

        Notes:
            - Leading zeros are automatically discarded (e.g., 100 → 1)
            - This method avoids converting the number to string
            - This is mathematically equivalent to digit reversal via iteration

        References:
            - https://math.stackexchange.com/questions/480068/how-to-reverse-digits-of-an-integer-mathematically

        Args:
            x (int): A positive integer (x > 0).

        Returns:
            The integer formed by reversing the digits of x.

        Raises:
            ValueError if x is not a positive integer.
        """

        if x < 0:
            raise ValueError("x must be non-negative")

        total_digits = SolutionMath._determine_total_of_digits(x)
        n = total_digits - 1  # Highest digit index (0-based)
        first_term = x * 10**n

        acc = 0
        for k in range(1, n + 1):
            acc += (x // 10**k) * 10**(n - k)

        return first_term - 99 * acc

class SolutionStr:
    """Check if an integer is a palindrome without converting to a string.

    This class provides a method to determine whether a given integer
    reads the same forward and backward, using only arithmetic operations.
    """

    def isPalindrome(self, x: int) -> bool:
        """Check if a number is palindrome

        Args:
            x (int): The number to check if it is a palindrome

        Returns:
            bool: True if it is a palindrome, false otherwise.
        """
        num_str = str(x)
        return num_str == num_str[::-1]
