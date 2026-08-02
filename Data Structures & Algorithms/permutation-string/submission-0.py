""" 
A not working solution. just keep for record

s1 = 'abcc'
-> 
s1_dict
{
    'a': 1,
    'b': 1,
    'c': 1,
}

s2 = 'eacbdd'
eaacbddaaa
   l
     r

window_dict = {
    'a': 1
    'c': 1
    'b': 1
}

"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # init
        l = 0
        window_dict = {}
        s1_dict = {}
        for c1 in s1:
            s1_dict[c1] = s1_dict.get(c1, 0) + 1

        # scan s2 with sliding window
        for r in range(len(s2)):
            window_dict[s2[r]] = window_dict.get(s2[r], 0) + 1

            # reset window
            if s2[r] not in s1_dict or window_dict[s2[r]] > s1_dict[s2[r]]:
                window_dict[s2[l]] -= 1
                l += 1
                if window_dict[s2[r]] == 0:
                    del window_dict[s2[r]]
            
            # check if permutation of string exist
            if window_dict == s1_dict:
                return True
        
        return False




        