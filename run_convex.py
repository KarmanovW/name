#!/usr/bin/env -S python3 -B
from r2point import R2Point
from convex import Void

print("Введите координаты первой точки отрезка")
Ax = float(input(" x -> "))
Ay = float(input(" y -> "))
print("Введите координаты второй точки отрезка")
Bx = float(input(" x -> "))
By = float(input(" y -> "))

f = Void(R2Point(Ax, Ay), R2Point(Bx, By))
try:
    while True:
        f = f.add(R2Point())
        print(f"S = {f.area()}, P = {f.perimeter()}, Count = {f.count()}")
        print()
except (EOFError, KeyboardInterrupt):
    print("\nStop")
