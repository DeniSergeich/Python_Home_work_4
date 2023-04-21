list = list(map(int, input("Введите количество ягод на всех кустах: ").split()))
max = 0
for i in range(len(list)-1):
    if list[i-2] + list[i-1] + list[i] > max:
        max = list[i-2] + list[i-1] + list[i]
print(max)