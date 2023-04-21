list = list(map(int, input("Введите количество ягод на всех кустах: ").split()))
max = 0
for i in range(len(list)):
    temp = list[i-2]+list[i-1]+list[i]
    if temp > max:
        max = temp    
print(max)
