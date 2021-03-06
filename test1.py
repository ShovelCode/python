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
big_number = math.factorial(20)
#sets
salespeople = {'joe', 'sarah', 'alex', 'kevin'}
managers = {'sam', 'rachel', 'alex'}
joe_status = 'joe' in salespeople #in set
both_status = salespeople & managers #intersection
all_people = salespeople | managers #union
only_sales = salespeople - managers #subtract
is_superset = salespeople > managers #superset
is_subset = salespeople < managers #subset
union_minus_intersection = salespeople ^ managers #exclude intersection
set_of_nums = {x * x for x in range(10)} #set comprehension, not a list
a = 9
b = 7
#in line switch
a, b = b, a

class SwitchExample:
    def __init__(self) -> None:
        self.name = "la"
        self.a = 9
        self.b = 7
    def info(self):
        return ('testing')

rec1 = SwitchExample
#keep only one print statement
print(rec1.info) #outputs from class

