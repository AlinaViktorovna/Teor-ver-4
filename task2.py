# Задача 2.
# О случайной непрерывной равномерно распределенной величине B известно, что ее
# дисперсия равна 0.2. Можно ли найти правую границу величины B и ее среднее значение
# зная, что левая граница равна 0.5? Если да, найдите ее.

import math

# Параметры
variance_B = 0.2
a = 0.5

# Найдем правую границу b
b = a + math.sqrt(12 * variance_B)

# Среднее значение
mean_B = (a + b) / 2

print(f"Правая граница: {b:.2f}")
print(f"Среднее значение: {mean_B:.2f}")