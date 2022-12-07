l_1 = [1,11,14,5,8,9]
new_list = []

# for i in l_1:
#     if i < 10:
#         new_list.append(i)
# print(new_list)

newlist = [i for i in l_1 if i < 10]
print(newlist)

names1 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 'bob', 'kevin']
# print(sorted(names1, key=len))
# print(sorted(names1, key=len>4))
new_name = [name.title() for name in names1 if len(name) >= 4]
print(new_name)

# Bonus Challenge
names2 = ['connor', 'connor', 'bob', 'connor', 'evan', 'max', 'evan', 2, 2, 2, 3, 3, 4, 'bob', 'kevin']
new_name2 = [name.title() for name in names2 if type(name) == str and len(name) >= 4 ]
print(new_name2)


