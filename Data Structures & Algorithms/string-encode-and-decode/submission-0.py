"""
Seen video, will update this later.

Intuition: see the example below

encoding: ["abc3, def"] -> "4#abc33#def"
decoding: see the code
i = 1 + 5 = 6
"""

class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += "{}#{}".format(len(s), s)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        strs = []
        while i < len(s):
            digit_str = ''
            while s[i] != '#':
                digit_str += s[i]
                i += 1
            digit = int(digit_str)
            strs.append(s[i + 1 : i + 1 + digit])
            i += digit + 1
        return strs
