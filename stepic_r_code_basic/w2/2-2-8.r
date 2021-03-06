# Визуальная инспекция данных -- важный этап предварительного анализа данных. Она позволяет заметить очевидные несоответствия и аномалии в данных, и, что немаловажно, "почувствовать" структуру дата фрейма. Какие в нём есть переменные? Что они означают? В каких единицах измеряются? Какой у них диапазон значений?

# Используйте вспомогательные функции, о которых я говорил, чтобы разглядеть встроенный дата фрейм с названием quakes. Сопоставьте значения из этого дата фрейма и их описания.

# Подсказки:

# описание дата фрейма есть в справке: ?quakes
# медиана -- одна из описательных статистик; медиана и среднее -- разные вещи!


# 311.371
# 6.4
# 43
# 247
# 14
# 4

# Средняя глубина землетрясений (км)
# Максимальная сила землетрясений по шкале Рихтера
# Количество станций, зарегистрировавших землетрясение, записанное третьим
# Медианная глубина землетрясений (км)
# Количество станций, зарегистрировавших землетрясение, записанное предпоследним
# Минимальная сила землетрясений по шкале Рихтера

quakes = quakes[order(quakes$mag, decreasing = TRUE),]
print(quakes[quakes$mag >= 6.0,])
