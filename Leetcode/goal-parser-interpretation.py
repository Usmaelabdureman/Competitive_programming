"""
Goal Parser Interpretation
Easy

1485

85

Add to List

Share
You own a Goal Parser that can interpret a string command. The command consists of an alphabet of "G", "()" and/or "(al)" in some order. The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". The interpreted strings are then concatenated in the original order.

Given the string command, return the Goal Parser's interpretation of command.

 

Example 1:

Input: command = "G()(al)"
Output: "Goal"
Explanation: The Goal Parser interprets the command as follows:
G -> G
() -> o
(al) -> al
The final concatenated result is "Goal".
Example 2:

Input: command = "G()()()()(al)"
Output: "Gooooal"
Example 3:

Input: command = "(al)G(al)()()G"
Output: "alGalooG"
 

Constraints:

1 <= command.length <= 100
command consists of "G", "()", and/or "(al)" in some order.
Accepted
218,567
Submissions
251,685
Seen this question in a real interview before?

Yes

No
You need to check at most 2 characters to determine which character comes next.



1678/2950


Autocomplete





1
class Solution:
2
    def interpret(self, command: str) -> str:
3
            
    """
    
# Solution
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()','o').replace('(al)','al')
    
test =Solution()

cmd ="G()(al)"
print(test.interpret(cmd))

txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three", 1)

print(x)

# Python Assignment Operators

