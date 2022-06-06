class Solution(object):
    def nearestValidPoint(self, x, y, points):
        """
        :type x: int
        :type y: int
        :type points: List[List[int]]
        :rtype: int
        """
        
        temp = []
        for _ in points:
            if x == _[0] or y == _[1]:
                temp.append(_)
        
        res = {}
        for _ in temp:
            res[points.index(_)] = abs(_[0]-x) + abs(_[1] - y)
        
        
        res = sorted(res.items(), key=lambda res: res[1])
        
        if res == []: 
            return -1
        
        return res[0][0]
