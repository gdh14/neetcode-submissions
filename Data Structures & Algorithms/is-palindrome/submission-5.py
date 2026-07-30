""" 
Final clean solution, O(1) space.
"""

class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        while left < right:
            # 跳过左侧非字母数字
            while left < right and not s[left].isalnum():
                left += 1
            # 跳过右侧非字母数字
            while left < right and not s[right].isalnum():
                right -= 1

            # 比较（忽略大小写）
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True
