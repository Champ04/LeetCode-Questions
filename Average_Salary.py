class Solution(object):
    def average(self, salary):
        """
        :type salary: List[int]
        :rtype: float
        """
        
        salary = sorted(salary)
        res = salary[1:-1]
        return sum(res)/float(len(res))
        
