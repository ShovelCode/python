#this comment is a test for GitHub connection.
#this comment from laptop
print(9 ** 2)
list1 = [x ** 2 for x in range(10)]
print(list1)

list2 = [x + y for x in 'spam' for y in 'SPAM']

print(list2)

list3 = []
for x in range(10):
    if x % 2 == 0:
        for y in range(10):
            if y % 2 == 1:
                list3.append((x,y))

print(list3)
