import sys
import math
import random
import pickle #TODO eed to use this, aslo do a JSON coversion

def block1():
    print(sys.platform)
    print("from shob.py")
    print('hi' * 8)
    print(123 + 222)  # integers
    print(1.5 * 4)  # floating points
    print(2 ** 100)  # to the power  of
    print(dict(hours=10))  # dictionary iiteral
    print(math.pi)
    print(math.sqrt(85))
    print(random.random())  # between zero and one
    print(random.choice([1, 2, 3, 4]))  # random choice from a list literal
    s = 'spam'  # string literal
    print(s[-2])  # second to last character
    M = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # linear representation of a matrix literal, a Python list
    print(M[1])
    print(M[1][2])
    evens = [row[1] for row in M if row[1] % 2 == 0]  # list comprehension that produces a list of evens from row 1
    print(evens)
    '''f = open('data.txt', w)
    f.write('yes')
    f.write('no')
    text = f.read()'''  # multiline comment
    # print(text)
    # f.close()
    # add set operations

    L = [1, 2, 3]
    M = L  # rewrote it
    L == M  # value compare
    L is M  # object compare

    BigS = '''Multiline string
    literals are handy for handling JSONs
    and other XML files'''
    print(BigS)

    #TODO make this work right
    BigS.replace('i', 'y')  # replace all
    print(BigS)
    print(map(ord, BigS))

def block2():
    print("in block 2")

    #A multidimensional list, representing a tree
    L = ['abc', [(1,2), ([3], 4)], 5]
    print(L[1][1][0][0])
    log = open('data.txt', 'a') #What is a stand for?
    while True:
        reply = input('Enter data:' )
        if reply == 'stop': break
        try:
            print(int(reply) ** 2)
            print(reply, log)
        except:
            print('Bad!' * 8)
    print('Bye"')
    log.close()

    x = 'spam'
    while x:
        print(x)
        x = x[1:]
    #TODO did that work?

def block3():
    T = [(1,2), (3,4), (5,6)]
    for (a,b) in T:
        print(a, b)

    res = [ord(x) for x in 'tulips and daphodils']
    print(res)



# block1()
#block2()
block3()
