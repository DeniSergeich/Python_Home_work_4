list_1 = list(map(int, input("Введите список 1: ").split()))
list_2 = list(map(int, input("Введите список 2: ").split()))
list = set(list_1 + list_2)
print(list)