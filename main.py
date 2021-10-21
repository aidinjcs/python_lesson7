
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

a = (1, 2, [1, 4],)  # создали объект с типом данных кортеж и присвоили ему переменную
print(id(a))  # вывели id объекта
a[2].append(3)
print(a)
print(id(a))
a = (1, 3, [1, 4],)
print(id(a))

t = (5, 4, [3, 5],)
print(id(t))

print(t)
print(id(t))
tup = (5, 4, [3, 5],)
print(tup.count(t))

d = {"1":1}
d['1'] = 2
print(d)
d.clear()
print(d)

d = {"3":1}
d['3'] = 5
print(d)
d.copy()
print(d)

d = {"5": 4}
d['5'] = 3
print(d)
d.get(5)
print(d)


d = {'a': 1, 'b': 2, 'c': 3}
d.items()
print(d)

d = {'a': 2, 'b': 2}
d.keys()
print(d)


d = {'algebra': 5, 'literatura': 4}
print(d.values())

d = {'algebra': 5, 'literatura': 4}
d.update({'notebook': 5})
print(d)

d = {'audi', 'mustang'}
d.pop()
print(d)


d = {'audi', 'mustang'}
x = dict.setdefault
print(d)
