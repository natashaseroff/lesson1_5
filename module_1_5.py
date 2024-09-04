immutable_var = 1, 2, 'hello'
print(immutable_var)
#immutable_var [0] = 3
#print(immutable_var) #кортеж не поддерживает обращение к элементам
mutable_list = [1, 2, 'car', 'bike', 'train', '7800']
print(mutable_list)
mutable_list [2] = 'airplane'
print(mutable_list)