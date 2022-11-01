# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

list = [int]
for i in range(3):
    list.append(int(input('Введите 0 или 1: ')))

for i in list:
    left = not (list[0] or list[1] or list[2])
    right = (not list[0]) and (not list[1]) and (not list[2])

if left == right:
    print('True')
else:
    print('False')
