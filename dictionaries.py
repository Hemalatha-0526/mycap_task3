# empty dictionary
my_dict = {}

# dictionary with integer keys
my_dict1= {1: 'apple', 2: 'ball'}


# dictionary with mixed keys
my_dict2= {'name': 'John', 1: [2, 4, 3]}
print(my_dict2)
#output:{name:'John',1:[2,4,3]}


# using dict()
my_dict3= dict({1:'apple', 2:'ball'})
print(my_dict3)
#output:{1:'apple', 2:'ball'}

# from sequence having each item as a pair
my_dict4= dict([(1,'apple'), (2,'ball')])
print(my_dict4)
#output:1:{'apple', 2:'ball'}
print(my_dict.get(2))
#output:ball
