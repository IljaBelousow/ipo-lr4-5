spisok = []
num = int(input("введите количество чисел "))
for i in range(num):#запрашивает числа num раз
    a = int(input("число "))
    spisok.append(a)
nom = 0
max = spisok[0]
while nom < len(spisok):#пока nom меньше длины списка nom + 1
    if spisok[nom] > max:#если число по индексу nom больше максимального то оно становится максимальным
        max = spisok[nom]
    nom = nom + 1
print(max)
