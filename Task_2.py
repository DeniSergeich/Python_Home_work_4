list = list(map(int, input("Введите количество ягод на всех кустах: ").split()))
max = 0
for i in range(len(list)-1):
    if list[i-1] + list[i] + list[i+1] > max:
        max = list[i-1] + list[i] + list[i+1]
if list[-2] + list[-1] + list[0] > max:
        max = list[-2] + list[-1] + list[0]
print(max)