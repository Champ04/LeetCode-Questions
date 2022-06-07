class Solution(object):
    def areAlmostEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        match = 0
        mismatch = 0
        mismatch_index = []
        for _ in range(len(s1)):
            if s1[_] != s2[_]:
                mismatch+=1
                mismatch_index.append(_)
            
            else:
                match+=1
        
        if match == len(s1):
            return True
        
        if mismatch != 0 and mismatch > 2:
            return False
        elif mismatch == 1:
            return False
        else:
            if s1[mismatch_index[0]] == s2[mismatch_index[1]] and \
                s1[mismatch_index[1]] == s2[mismatch_index[0]]:
                return True
            else:
                return False
