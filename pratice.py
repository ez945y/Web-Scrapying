import random
data = {'a':'A','b':'B','c':'C','d':'D'}
dict2 = dict(Mike=2)
print(random.choice(list(data.items())))
print(random.choice(list(data.keys())))
print(random.choice(list(data.values())))
print(type(list(dict2.keys())[0]))