immutable_var = 1, 'a', 2, 'b'
mutable_list = [1, 2, 'b', 'a']
print(immutable_var)
print(mutable_list)
#immutable_var[3] = 'error' кортеж является неизменяемым типом данных, здесь будет ошибка
mutable_list.append('succes')
print(mutable_list)