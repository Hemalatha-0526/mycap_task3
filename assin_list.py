#Assigning Elements in a list

list1=['java','C','python','C#','lisp']
list2=[1,2,3,4,5]
list3=['a','aa','aaa']

#Accessing Elements in a list

print(list1)
print(list2)
print(list3)

#output:
#['java','C','python','C#','lisp']
#[1,2,3,4,5]
#['a','aa','aaa']

del list2[3]
print(list3)

#output:
#['a','aa']

list3[1:3]
#output:['aa']
list[1:]
#output:['C', 'python', 'C#', 'lisp']
