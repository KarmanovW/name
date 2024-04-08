#!/usr/bin/env -S python3 -B
from tk_drawer import TkDrawer
from r2point import R2Point
from convex import Void, Point, Segment, Polygon


def void_draw(self, tk):
    tk.draw_line(self._snippet.A, self._snippet.B, "red")


def point_draw(self, tk):
    tk.draw_point(self.p)
    tk.draw_line(self._snippet.A, self._snippet.B, "red")


def segment_draw(self, tk):
    tk.draw_line(self.p, self.q)
    tk.draw_line(self._snippet.A, self._snippet.B, "red")


def polygon_draw(self, tk):
    for n in range(self.points.size()):
        tk.draw_line(self.points.last(), self.points.first())
        self.points.push_last(self.points.pop_first())
    tk.draw_line(self._snippet.A, self._snippet.B, "red")


setattr(Void, 'draw', void_draw)
setattr(Point, 'draw', point_draw)
setattr(Segment, 'draw', segment_draw)
setattr(Polygon, 'draw', polygon_draw)


tk = TkDrawer()
print("Введите координаты первой точки отрезка")
Ax = float(input(" x -> "))
Ay = float(input(" y -> "))
print("Введите координаты второй точки отрезка")
Bx = float(input(" x -> "))
By = float(input(" y -> "))

f = Void(R2Point(Ax, Ay), R2Point(Bx, By))
tk.clean()
f.draw(tk)

try:
    while True:
        f = f.add(R2Point())
        tk.clean()
        f.draw(tk)
        print(f"S = {f.area()}, P = {f.perimeter()}, Count = {f.count()}\n")
except (EOFError, KeyboardInterrupt):
    print("\nStop")
    tk.close()
