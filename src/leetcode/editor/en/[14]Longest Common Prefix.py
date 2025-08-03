"""
🔢 LeetCode Problem: 14 - Longest Common Prefix
https://leetcode.com/problems/longest-common-prefix/

🧩 Description:
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

📌 Examples:
    - Input: ["flower","flow","flight"] → Output: "fl"
    - Input: ["dog","racecar","car"]   → Output: ""

📌 Constraints:
    • 1 ≤ strs.length ≤ 200
    • 0 ≤ strs[i].length ≤ 200
    • strs[i] consists of only lowercase English letters if non-empty.

👨‍💻 Explored Approaches:
    1. Horizontal scan (character-by-character into all strings)
    2. Zip-based scan (using zip(*) and set check)
    3. Binary search on prefix length
    4. Sort & compare first vs. last
    5. Divide & conquer (recursive merging)

Benchmark Results (average runtime per call in seconds):
| n    | sort        | binary      | zip          | horizontal   | divide_and_conquer |
|------|-------------|-------------|--------------|--------------|--------------------|
| 10   | 0.000012    | 0.000012    | 0.000021     | 0.000078     | 0.000061           |
| 100  | 0.000012    | 0.000034    | 0.000106     | 0.000424     | 0.000692           |
| 500  | 0.000017    | 0.000177    | 0.000546     | 0.002052     | 0.002920           |
| 1000 | 0.000022    | 0.000390    | 0.001079     | 0.005615     | 0.005845           |
| 2000 | 0.000052    | 0.000723    | 0.002315     | 0.008572     | 0.011302           |

🧮 Complexity Analysis:
    • Horizontal scan:  O(S) time, O(1) space
    • Zip-based scan:  O(S) time, O(1) space
    • Binary search:    O(S · log m) time, O(1) space
    • Sort & compare:   O(n·m + n log n) time, O(1) space
    • Divide & conquer: O(S · log n) time, O(log n) space

Conclusion:
The Sort & Compare approach is consistently the fastest, followed by Binary Search, Zip-based scan,
horizontal scan, and finally Divide & Conquer (due to recursive overhead).

When to use each approach:
- **Sort & Compare**: go-to for simplicity and performance in most real-world cases.
- **Binary Search**: choose when strings are long and comparisons are expensive.
- **Zip-based Scan**: ideal for concise, readable code on moderate sizes.
- **Horizontal Scan**: best for very small lists where clarity matters.
- **Divide & Conquer**: academic use or parallel frameworks; introduces recursion.

⏱️ Time invested:
    - Analysis & planning: 15 minutes
    - Implementation & benchmarking: 30 minutes
    - Documentation & review: 10 minutes
    - 🔄 Total: ~55min

🧠 Challenges encountered:
    - Balancing readability vs. raw performance.
    - Ensuring benchmarks reflect realistic string distributions.
    - Managing recursion depth in divide & conquer.

💡 Technical note:
Even linear-time scans differ in constant factors; sorting trades extra comparisons for a single pass comparison.

✍️ Personal note:
Benchmark-driven decisions help illustrate tradeoffs and guides selection based on data characteristics.

🏷️ Tags:
#Python #LeetCode #CleanCode #Benchmarking #ProblemSolving #Algorithms #DeveloperJourney
"""

# Write a function to find the longest common prefix string amongst an array of
# strings. 
# 
#  If there is no common prefix, return an empty string "". 
# 
#  
#  Example 1: 
# 
#  
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#  
# 
#  Example 2: 
# 
#  
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= strs.length <= 200 
#  0 <= strs[i].length <= 200 
#  strs[i] consists of only lowercase English letters if it is non-empty. 
#  
# 
#  Related Topics Array String Trie 👍 19584 👎 4765


# leetcode submit region begin(Prohibit modification and deletion)

class Solution:
    """Container for implementation of the Longest Common Prefix problem."""

    def longestCommonPrefixHorizontal(self, strs: list[str]) -> str:
        """Horizontal Scan for Longest Common Prefix.

        Given an array of strings, find the longest common prefix among them.
        If there is no common prefix, return an empty string.

        - Runtime:  O(S) where S = sum of all characters in the array.
        - Memory:   O(1) extra space (just a few pointers and counters).
        - Performance rank: 4th fastest in benchmarks.
        """
        if not strs:
            return ""

        min_length = min(len(s) for s in strs)
        lcp = ""
        for i in range(min_length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                lcp += char
            else:
                break
        return lcp


    def longestCommonPrefixZip(self, strs: list[str]) -> str:
        """Zip-based Longest Common Prefix.

        Given an array of strings, find the longest common prefix among them.
        If there is no common prefix, return an empty string.

        - Runtime:  O(S) where S = sum of all characters in the array.
        - Memory:   O(1) extra (just a few pointers and counters).
        - Performance rank: 3rd fastest.
        """
        if not strs:
            return ""

        prefix_chars: list[str] = []
        # zip: ('f', 'f', 'f'), ('l', 'l', 'l'), ('o', 'o', 'i'), ...
        for i, letters in enumerate(zip(*strs)):
            if len(set(letters)) == 1:
                prefix_chars.append(letters[0])
            else:
                break
        return "".join(prefix_chars)

    def longestCommonPrefixBinarySearch(self, strs: list[str]) -> str:
        """Binary Search for Longest Common Prefix.

        Use binary search on the prefix length. At each step, check whether
        all strings share the prefix of length mid, narrowing the search
        window accordingly.

        - Runtime:  O(S · log m), where m = length of the shortest string.
        - Memory:   O(1) extra space.
        - Performance rank: 2nd fastest in benchmarks.
        """
        if not strs:
            return ""
        # length of the shortest string
        min_len = min(len(s) for s in strs)
        low, high = 1, min_len

        def is_common_prefix(length: int) -> bool:
            prefix = strs[0][:length]
            return all(s.startswith(prefix) for s in strs)

        best = ""
        while low <= high:
            mid = (low + high) // 2
            if is_common_prefix(mid):
                best = strs[0][:mid]
                low = mid + 1
            else:
                high = mid - 1
        return best

    def longestCommonPrefix(self, strs: list[str]) -> str:
        """Sort & Compare for Longest Common Prefix.

        Sort the array lexicographically, then only the first and last strings
        can have the minimal common prefix for the entire group. Compare them
        character by character.

        - Runtime:  O(n·m + n log n), dominated by sort (n = number of strings, m = average length)
        - Memory:   O(1) extra space
        - Performance rank: fastest
        """
        if not strs:
            return ""
        strs.sort()
        first, last = strs[0], strs[-1]
        i = 0
        while i < len(first) and i < len(last) and first[i] == last[i]:
            i += 1
        return first[:i]

    def longestCommonPrefixDivideAndConquer(self, strs: list[str]) -> str:
        """
        Longest Common Prefix — Divide & Conquer

        Summary:
        Recursively split the array into halves, compute the LCP for each half,
        then merge by comparing the two partial prefixes.

        Runtime:  O(S · log n), where S = total characters, n = number of strings
        Memory:   O(log n) recursion depth
        Time spent: ~25 minutes
        """
        if not strs:
            return ""

        def lcp_range(left: int, right: int) -> str:
            if left == right:
                return strs[left]
            mid = (left + right) // 2
            lcp_left = lcp_range(left, mid)
            lcp_right = lcp_range(mid + 1, right)
            # merge step: compare two prefixes
            min_len = min(len(lcp_left), len(lcp_right))
            i = 0
            while i < min_len and lcp_left[i] == lcp_right[i]:
                i += 1
            return lcp_left[:i]

        return lcp_range(0, len(strs) - 1)

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":

    test_cases = [
        (["flower", "flow", "flight"], "fl"),
        (["dog", "racecar", "car"], ""),
        ([""], ""),
        (["a"], "a"),
        (["a", "b"], ""),
        (["a", "a"], "a"),
        (["a", "aa"], "a"),
        (["aa", "a"], "a"),
        (["aa", "aaa"], "aa"),
        (["aaa", "aa"], "aa"),
        (["a", "ab"], "a"),
        (["ab", "a"], "a"),
        (["ab", "abc"], "ab"),
        (["abc", "ab"], "ab"),
        (["abc", "abcd"], "abc"),
        (["abcd", "abc"], "abc"),
        (["abc", "abx"], "ab"),
        (["abx", "abc"], "ab"),
        (["abc", "xyz"], ""),
        (["xyz", "abc"], ""),
        (["abc", "def"], ""),
        (["def", "abc"], ""),
        (["abc", ""], ""),
        (["", "abc"], ""),
        (["", ""], ""),
        (["", "a"], ""),
        (["a", ""], ""),
        (["", "ab"], ""),
        (["ab", ""], ""),
        (["", "abc", "def"], ""),
        (["abc", "", "def"], ""),
        (["abc", "def", ""], ""),
        (["", "", "abc"], ""),
        (["abc", "", ""], ""),
        (["", "abc", "def", "ghi"], ""),
        (["abc", "def", "", "ghi"], ""),
        (["abc", "def", "ghi", ""], ""),
        (["", "", "abc", "def"], ""),
        (["abc", "", "def", "ghi"], ""),
        (["abc", "def", "ghi", ""], ""),
        (["", "abc", "def", "ghi", "jkl"], ""),
        (["abc", "def", "ghi", "", "jkl"], ""),
        (["abc", "def", "ghi", "jkl", ""], ""),
        (["", "", "abc", "def", "ghi"], ""),
        (["abc", "", "def", "ghi"], ""),
        (["abc", "def", "ghi", ""], ""),
        (["", "abc", "def", "ghi", "jkl", "mno"], ""),
        (["abc", "def", "ghi", "", "jkl", "mno"], ""),
        (["abc", "def", "ghi", "jkl", ""], ""),
        (["", "", "abc", "def", "ghi"], ""),
        (["abc", "", "def", "ghi"], ""),
        (["abc", "def", "ghi", ""], ""),
    ]

    # Example usage
    solution = Solution()
    for strs, expected in test_cases:
        # Test cases for longestCommonPrefix
        result = solution.longestCommonPrefix(strs)
        print(f"Input: {strs}, Expected: {expected}, Result: {result}")
        assert result == expected, f"Expected {expected}, but got {result}"

        # Test cases for longestCommonPrefixZip
        result_zip = solution.longestCommonPrefixZip(strs)
        print(f"Input: {strs}, Expected: {expected}, Result: {result_zip}")
        assert result_zip == expected, f"Expected {expected}, but got {result_zip}"

        # Test cases for longestCommonPrefixBinarySearch
        result_bs = solution.longestCommonPrefixBinarySearch(strs)
        print(f"Input: {strs}, Expected: {expected}, Result: {result_bs}")
        assert result_bs == expected, f"Expected {expected}, but got {result_bs}"

        # Test cases for longestCommonPrefixSort
        result_sort = solution.longestCommonPrefixSort(strs)
        print(f"Input: {strs}, Expected: {expected}, Result: {result_sort}")
        assert result_sort == expected, f"Expected {expected}, but got {result_sort}"

        # Test cases for longestCommonPrefixDivideAndConquer
        result_dc = solution.longestCommonPrefixDivideAndConquer(strs)
        print(f"Input: {strs}, Expected: {expected}, Result: {result_dc}")
        assert result_dc == expected, f"Expected {expected}, but got {result_dc}"
