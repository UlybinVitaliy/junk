# # Задача: считайте данные из файла и посчитайте их средние значения.

# На вход вашему решению будет подан адрес, по которому расположен csv-файл, из которого нужно считать данные. Первая строчка в файле — названия столбцов, остальные строки — числовые данные (то есть каждая строка, кроме первой, состоит из последовательности вещественных чисел, разделённых запятыми).

# Посчитайте и напечатайте вектор из средних значений вдоль столбцов входных данных. То есть если файл с входными данными выглядит как

# a,b,c,d
# 1.5,3,4,6
# 2.5,2,7.5,4
# 3.5,1,3.5,2

# то ответом будет

# [ 2.5  2.   5.   4. ]

# Как упоминалось на предыдущем шаге, в качестве файла для loadtxt можно передать объект файла. Это удобно в таких случаях, как сейчас: когда данные лежат не на вашем компьютере, а где-то в сети. Как их скачать из сети? С помощью стандартных библиотек:

# >>> from urllib.request import urlopen
# >>> f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')


# Теперь в f содержится объект файла, который можно передать в loadtxt.

# Sample Input:

# https://stepic.org/media/attachments/lesson/16462/boston_houses.csv

# Sample Output:

# [ 22.53280632   3.61352356  11.36363636   0.06916996   0.55469506
#    6.28463439   3.79504269]

# 4 Check
# from urllib.request import urlopen
# f = urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')
# sbux = np.loadtxt(f,skiprows=1, delimiter=",")
# print(sbux.mean(axis=0))

from urllib.request import urlopen
import numpy as np

filename = input()
f = urlopen(filename)
sbux = np.loadtxt(f,skiprows=1, delimiter=",")
print(sbux.mean(axis=0))