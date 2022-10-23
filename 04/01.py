# Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

from decimal import Decimal
import math

print(Decimal(math.pi).quantize(Decimal(input('Введите точность округления: '))))
