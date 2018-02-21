'''
https://www.hackerrank.com/challenges/balanced-brackets

Sample Input

3
{[()]}
{[(])}
{{[[(())]]}}

Sample Output

YES
NO
YES

((())))))
(((())

NO
NO

()()()
(())[[]]{{{}}}
YES
YES

)(
---
stack = []
for bracket in input:
    if it's an open bracket, push the bracket.
    if it's a close bracket, pop.
        If the popped bracket doesn't match the closing bracket,
        print NO
If the stack isn't empty:
    print NO
print YES
'''

bracket_map = {'{': '}', '[': ']', '(': ')'}
opening_brackets = bracket_map.keys()
closing_brackets = bracket_map.values()


def solver(test_string):
    stack = []
    try:
        for bracket in test_string:
            if bracket in opening_brackets:
                stack.append(bracket)
            elif bracket in closing_brackets:
                expected_opening_bracket = stack.pop()
                assert bracket_map[expected_opening_bracket] == bracket
        assert not stack
        print 'YES'
    except (IndexError, AssertionError):
        print 'NO'
