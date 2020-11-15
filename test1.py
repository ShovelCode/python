''' 
big block comment
Python 3.x reserved words
False class finally is return
None continue for lambda try
True def from nonlocal while
and del global not with
as elif if or yield 
assert else import pass
break except in raise '''
import math
import json #not used

def scramble(seq):
    res = []
    for i in range(len(seq)):
        res.append(seq[i:] + seq[:i])
    return res

reserved_words = set(['False', 'class', 'finally', 'is', 'return', 'None', 'continue', 'for', 'lambda', 'try', 'True', 'def', 'from', 'nonlocal', 'while', 'and', 'del', 'global', 'not', 'with', 'as', 'elif', 'if', 'or', 'yield', 'assert', 'else', 'import', 'pass', 'break', 'except', 'in', 'raise'])
reserved_words_check = 'until' in reserved_words #not Perl
four_squares = [x * 2 for x in [abs(x) for x in (-1,-2,3,4)]]
scrambled_eggs = scramble('eggs')
#keep only one print statement
print(scrambled_eggs)

