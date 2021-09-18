import math
print("Введите значения длин сторон")
print("a=? ")
a=int(input())
print("b=? ")
b=int(input())
print("γ=? ")
γ=int(input())
print(math.sqrt(a*a+b*b-2*a*b*math.cos(math.radians(γ))))


