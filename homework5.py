immutable_var = (32, 'start', 74, 'temp')
print(immutable_var)
# immutable_var[0] = 23
# print(immutable_var) # Кортеж хранит ссылку на список, а не сам список. Поэтому его нельзя изменить.

mutable_list = (["stop", 42], 'door', 20)
print(mutable_list)
mutable_list[0][0] = 'start'
mutable_list[0][1] = 24
print(mutable_list)