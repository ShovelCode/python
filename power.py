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