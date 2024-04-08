from deq import Deq
from r2point import R2Point


class Figure:
    """ Абстрактная фигура """

    def perimeter(self):
        return 0.0

    def area(self):
        return 0.0

    def count(self):
        return 0


class Void(Figure):
    """ "Hульугольник" """
    def __init__(self, A, B):
        self._snippet = Snippet(A, B)

    def add(self, p):
        return Point(p, self._snippet)


class Point(Figure):
    """ "Одноугольник" """

    def __init__(self, p, _snippet):
        self.p = p
        self._snippet = _snippet

    def add(self, q):
        return self if self.p == q else Segment(self.p, q, self._snippet)

    def count(self):
        if self._snippet.distant(self.p):
            return 1
        else:
            return 0


class Segment(Figure):
    """ "Двуугольник" """

    def __init__(self, p, q, _snippet):
        self.p, self.q = p, q
        self._snippet = _snippet

    def perimeter(self):
        return 2.0 * self.p.dist(self.q)

    def add(self, r):
        if R2Point.is_triangle(self.p, self.q, r):
            return Polygon(self.p, self.q, r, self._snippet)
        elif r.is_inside(self.p, self.q):
            return self
        elif self.p.is_inside(r, self.q):
            return Segment(r, self.q, self._snippet)
        else:
            return Segment(self.p, r, self._snippet)

    def count(self):
        if self._snippet.distant(self.p):
            if self._snippet.distant(self.q):
                return 2
            else:
                return 1
        else:
            if self._snippet.distant(self.q):
                return 1
            else:
                return 0


class Polygon(Figure):
    """ Многоугольник """

    def __init__(self, a, b, c, _snippet):
        self._snippet = _snippet
        self.points = Deq()
        self.points.push_first(b)
        if b.is_light(a, c):
            self.points.push_first(a)
            self.points.push_last(c)
        else:
            self.points.push_last(a)
            self.points.push_first(c)
        self._perimeter = a.dist(b) + b.dist(c) + c.dist(a)
        self._area = abs(R2Point.area(a, b, c))
        self._count = 0
        if self._snippet.distant(a):
            self._count += 1
        if self._snippet.distant(b):
            self._count += 1
        if self._snippet.distant(c):
            self._count += 1

    def perimeter(self):
        return self._perimeter

    def area(self):
        return self._area

    def count(self):
        return self._count

    # добавление новой точки
    def add(self, t):

        # поиск освещённого ребра
        for n in range(self.points.size()):
            if t.is_light(self.points.last(), self.points.first()):
                break
            self.points.push_last(self.points.pop_first())

        # хотя бы одно освещённое ребро есть
        if t.is_light(self.points.last(), self.points.first()):

            # учёт удаления ребра, соединяющего конец и начало дека
            self._perimeter -= self.points.first().dist(self.points.last())
            self._area += abs(R2Point.area(t,
                                           self.points.last(),
                                           self.points.first()))

            # удаление освещённых рёбер из начала дека
            p = self.points.pop_first()
            while t.is_light(p, self.points.first()):
                self._perimeter -= p.dist(self.points.first())
                self._area += abs(R2Point.area(t, p, self.points.first()))
                if self._snippet.distant(p):
                    self._count -= 1
                p = self.points.pop_first()
            self.points.push_first(p)

            # удаление освещённых рёбер из конца дека
            p = self.points.pop_last()
            while t.is_light(self.points.last(), p):
                self._perimeter -= p.dist(self.points.last())
                self._area += abs(R2Point.area(t, p, self.points.last()))
                if self._snippet.distant(p):
                    self._count -= 1
                p = self.points.pop_last()
            self.points.push_last(p)

            # добавление двух новых рёбер
            self._perimeter += t.dist(self.points.first()) + \
                t.dist(self.points.last())
            self.points.push_first(t)
            if self._snippet.distant(t):
                self._count += 1

        return self


class Snippet:
    '''Проверка лежит лм точка в 1 окрестности отрезка'''
    def __init__(self, a, b):
        self.A = a
        self.B = b

    def distant(self, Q):
        AQx = Q.x - self.A.x
        AQy = Q.y - self.A.y
        ABx = self.B.x - self.A.x
        ABy = self.B.y - self.A.y
        BQx = Q.x - self.B.x
        BQy = Q.y - self.B.y
        BAx = self.A.x - self.B.x
        BAy = self.A.y - self.B.y

        if (AQx * ABx + AQy * ABy) * (BQx * BAx + BQy * BAy) <= 0:
            return min(self.A.dist(Q), self.B.dist(Q)) < 1
        else:
            return (abs(2 * R2Point.area(Q, self.A, self.B))
                    < self.A.dist(self.B))


if __name__ == "__main__":
    Ax = float(input(" x -> "))
    Ay = float(input(" y -> "))
    Bx = float(input(" x -> "))
    By = float(input(" y -> "))
    f = Void(R2Point(Ax, Ay), R2Point(Bx, By))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(1.0, 0.0))
    print(type(f), f.__dict__)
    f = f.add(R2Point(0.0, 1.0))
    print(type(f), f.__dict__)
