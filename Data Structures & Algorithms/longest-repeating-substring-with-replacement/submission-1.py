""" 
Sliding window (Optimal )

when to shrink left? when window_size > max_char_cnt + k

abcd

window_size = 4
k=2
max_char_cnt = 1


aabcda, k=2
 l
    r

char_cnt = {
    'a': 1,
    'b': 1,
    'c': 1,
    'd': 1
}
max_char_cnt = 2
k = 2
window_size = 4

"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_cnt = {}        
        max_char_cnt = 0
        res = 0
        l = 0
        for r in range(len(s)):
            # maintain char count in window / max char count
            if s[r] not in char_cnt:
                char_cnt[s[r]] = 1
            else:
                char_cnt[s[r]] += 1

            # this is how to keep max_char_cnt seen so far
            max_char_cnt = max(max_char_cnt, char_cnt[s[r]])

            # shrink left edge when window_size > max_char_cnt + k
            # why no need to update max_char_cnt?
            if (r - l + 1) > max_char_cnt + k:
                char_cnt[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
