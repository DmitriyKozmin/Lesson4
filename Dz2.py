n_bushes = int(input('Введите количество кустов черники: '))
list_1 = list()
for i in range(n_bushes):
    a =int(input('Введите количество ягод на кусте: '))
    list_1.append(a)

list_1_count = list()
for i in range(len(list_1)):
       list_1_count.append(list_1[i-2] + list_1[i-1] + list_1[i])
print(max(list_1_count))