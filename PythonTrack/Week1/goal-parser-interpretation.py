class Solution:
    def interpret(self, command: str) -> str:
        # I think this question's intention to utilize the replace mwthod of python in string method      
        return command.replace('()','o').replace('(al)','al')