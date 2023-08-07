n=int(input('Введите количество элементов в n: '))
m=int(input('Введите количество элементов в m: '))
n_list=[]
for i in range(n):
    x = int(input('Введите элемент списка n: '))
    n_list.append(x)
n_set = set(n_list)
m_list=[]
for i in range(m):
    y = int(input('Введите элемент списка m: '))
    m_list.append(y)
m_set = set(m_list)
s_set = sorted(n_set.intersection(m_set))
print(n_list)
print(m_list)
print(s_set)