#8th of 11 of 2020
#HP Laptop 1
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



name_for_userid = {
    382: "Alice",
    590: "Bob",
    951: "Dilbert",
}

def greeting(userid):
    return "Hi %s!" % name_for_userid.get(userid, "there")

greeting(382)

greeting(333333)

x, y, z = 0, 1, 0

if x == 1 or y == 1 or z == 1:
    print('passed')

if 1 in (x, y, z):
    print('passed')

# These only test for truthiness:
if x or y or z:
    print('passed')

if any((x, y, z)):
    print('passed')

result = 9 // 4 #floor division
result2 = 9 / 4 #classic division
result3 = (2 + 1j) * (3 + 2j) #complex number primitives
result4 = 'e' in set('abcdefg')
print(result)
print(result2)
print(result3)
print(result4)