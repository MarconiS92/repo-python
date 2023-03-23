name="John"
print("Hello "+ name)

print("Mar"*3)
print(list(range(4,10)))

ime="Marko"
prezime="Stanojevic"
print(ime,prezime)
print(ime*3,prezime*2)
print([1,2,3] + list(range(4,8))*3)
print("New York".index("Y"))
print('Moscow'.count('o'))
print("New York".split())
print("apple#banana#orange".split('#'))

a='5+7'
print(eval(a))

groups = [['student1', 'student2', 'student3'],
 
    ['student4', 'student5', 'student6'],
 
    ['student7', 'student8', 'student9'],
 
    ['student10', 'student11', 'student12']]
 
 
for group in groups:
    for student in group:
        print("Group: {},{}".format(groups.index(group),student),end = ', ')
    print('')