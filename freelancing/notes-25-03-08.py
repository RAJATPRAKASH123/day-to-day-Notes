def genPar(open, closed, expression):
	
	whenever at any point we are getting the expression, 
	we append that expression

	case 1: Function call requires - expression + (
	
	case 2: Function call ...

NOTE : Whenver we are asked to generate words/paranthesis, count ...


Ex - N=8 Queens : Put N queens such that noone kill each other.

........
........
Q.......
........
........
........
........
........

But, the problem : Every function call has to store its 
separate chess board config./permutations of Queens.
: Very expensive (Space Complexity)

How can we solve this situation?


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        '''
        n = 2
        '''
        expression = ""
        def generateParentheses(n, open_count=0, close_count=0):
            # Base case: if we've used exactly n pairs (2*n characters)
            if len(expression) == 2 * n:
                result.append(expression)
                return
            
            # Case 1: We can add an opening parenthesis if we haven't used all n
            if open_count < n:
            	# ()(())  n = 5
            	expression = expression + '('
                generateParentheses(n, open_count + 1, close_count)
                expression.deleteLastIndex('(');

            
            # Case 2: We can add a closing parenthesis if we have unclosed openings
            if close_count < open_count:
            	expression = expression + ')'
                generateParentheses(n, open_count, close_count + 1)
                expression.deleteLastIndex(')');

        
        generateParentheses(n)
        return result


        a + b + c ~= target  ---> O(n**3)

        a + b ~= target - c [Hashmap] ---> O(n**2)

        [. . . . . . . . . .]
          p1		     p2





