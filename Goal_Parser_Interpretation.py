class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        
        res = ''
        for i in range(len(command)):
            if command[i].upper() == 'G' or command[i:i+2] == 'G(':
                res+='G'
            elif command[i:i+2] == '()':
                res+='o'
                i+=2
            elif command[i:i+2] == '(a':
                res+='al'
                i+=4
            
        return res
