#Assigning Elements in a tuple

tup1=('java','C','python','C#','lisp')
tup2=(1,2,3,4,5)
tup3=('a','aa','aaa')

#Accessing Elements in a list

print(tup1)
print(tup2)
print(tup3)

#output:
#('java','C','python','C#','lisp')
#(1,2,3,4,5)
#('a','aa','aaa')

del tup2[3]

#output:type error since tuples are unmuttable


print(tup3)

#output:
#['a','aa']

print(tup2[0])
#output:
#1
tup3[1:3]
#output:('a','aa')
tup1[1:]
#output:('C', 'python', 'C#', 'lisp')
