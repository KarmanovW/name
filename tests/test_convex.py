from pytest import approx
from math import sqrt
from r2point import R2Point
from convex import Figure, Void, Point, Segment, Polygon, Snippet


class TestVoid:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Void(R2Point(0, 0), R2Point(1, 0))

    # Нульугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Void (нульугольник)
    def test_void(self):
        assert isinstance(self.f, Void)

    # Периметр нульугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь нульугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки нульугольник превращается в одноугольник
    def test_add(self):
        assert isinstance(self.f.add(R2Point(0.0, 0.0)), Point)

    # кол-во точек пустоты лежащих в 1 окрестности
    def test_snippet1(self):
        assert self.f.count() == 0

    # кол-во точек пустоты лежащих в 1 окрестности
    def test_snippet2(self):
        assert Void(R2Point(5, 4), R2Point(4, 5)).count() == 0


class TestPoint:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Point(R2Point(0.0, 0.0),
                       Snippet(R2Point(0, 0), R2Point(1, 0)))

    # Одноугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Point (одноугольник)
    def test_point(self):
        assert isinstance(self.f, Point)

    # Периметр одноугольника нулевой
    def test_perimeter(self):
        assert self.f.perimeter() == 0.0

    # Площадь одноугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки одноугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки одноугольник может превратиться в двуугольник
    def test_add2(self):
        assert isinstance(self.f.add(R2Point(1.0, 0.0)), Segment)

    # кол-во точек лежащих в 1 окрестности
    def test_snippet3(self):
        assert self.f.count() == 1

    # кол-во точек лежащих в 1 окрестности
    def test_snippet4(self):
        assert Point(R2Point(0.0, 0.0),
                     Snippet(R2Point(2, 2), R2Point(2, 3))).count() == 0


class TestSegment:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.f = Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0),
                         Snippet(R2Point(0, 0), R2Point(1, 0)))

    # Двуугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Segment (двуугольник)
    def test_segment(self):
        assert isinstance(self.f, Segment)

    # Периметр двуугольника равен удвоенной длине отрезка
    def test_perimeter(self):
        assert self.f.perimeter() == approx(2.0)

    # Площадь двуугольника нулевая
    def test_area(self):
        assert self.f.area() == 0.0

    # При добавлении точки двуугольник может не измениться
    def test_add1(self):
        assert self.f.add(R2Point(0.5, 0.0)) is self.f

    # Он не изменяется в том случае, когда добавляемая точка совпадает
    # с одним из концов отрезка
    def test_add2(self):
        assert self.f.add(R2Point(0.0, 0.0)) is self.f

    # При добавлении точки правее двуугольник может превратиться в другой
    # двуугольник
    def test_add3(self):
        assert isinstance(self.f.add(R2Point(2.0, 0.0)), Segment)

    # При добавлении точки левее двуугольник может превратиться в другой
    # двуугольник
    def test_add4(self):
        assert isinstance(self.f.add(R2Point(-1.0, 0.0)), Segment)

    # При добавлении точки двуугольник может превратиться в треугольник
    def test_add5(self):
        assert isinstance(self.f.add(R2Point(0.0, 1.0)), Polygon)

    # кол-во точек лежащих в 1 окрестности
    def test_snippet5(self):
        assert self.f.count() == 2

    # кол-во точек лежащих в 1 окрестности
    def test_snippet6(self):
        i = R2Point(1.0, 0.0)
        j = R2Point(3.0, 0.0)
        assert Segment(R2Point(1.0, 0.0), R2Point(7.0, 0.0),
                       Snippet(i, j)).count() == 1.0

    # кол-во точек лежащих в 1 окрестности
    def test_snippet7(self):
        i = R2Point(1.0, 0.0)
        j = R2Point(3.0, 0.0)
        assert Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0),
                       Snippet(i, j)).count() == 1.0

    # кол-во точек лежащих в 1 окрестности
    def test_snippet8(self):
        i = R2Point(8.0, 7.0)
        j = R2Point(9.0, 8.0)
        assert Segment(R2Point(0.0, 0.0), R2Point(1.0, 0.0),
                       Snippet(i, j)).count() == 0.0


class TestPolygon:

    # Инициализация (выполняется для каждого из тестов класса)
    def setup_method(self):
        self.a = R2Point(0.0, 0.0)
        self.b = R2Point(1.0, 0.0)
        self.c = R2Point(0.0, 1.0)
        self.f = Polygon(self.a, self.b, self.c,
                         Snippet(R2Point(0, 0), R2Point(1, 0)))

    # Многоугольник является фигурой
    def test_figure(self):
        assert isinstance(self.f, Figure)

    # Конструктор порождает экземпляр класса Polygon (многоугольник)
    def test_polygon1(self):
        assert isinstance(self.f, Polygon)

    # Изменение порядка точек при создании объекта всё равно порождает Polygon
    def test_polygon2(self):
        self.f = Polygon(self.b, self.a, self.c,
                         Snippet(R2Point(0, 0), R2Point(1, 0)))
        assert isinstance(self.f, Polygon)

    # Изменение количества вершин многоугольника
    #   изначально их три
    def test_vertexes1(self):
        assert self.f.points.size() == 3

    #   добавление точки внутрь многоугольника не меняет их количества
    def test_vertexes2(self):
        assert self.f.add(R2Point(0.1, 0.1)).points.size() == 3

    #   добавление другой точки может изменить их количество
    def test_vertexes3(self):
        assert self.f.add(R2Point(1.0, 1.0)).points.size() == 4

    #   изменения выпуклой оболочки могут и уменьшать их количество
    def test_vertexes4(self):
        assert self.f.add(
            R2Point(
                0.4,
                1.0)).add(
            R2Point(
                1.0,
                0.4)).add(
            R2Point(
                0.8,
                0.9)).add(
            R2Point(
                0.9,
                0.8)).points.size() == 7
        assert self.f.add(R2Point(2.0, 2.0)).points.size() == 4

    # Изменение периметра многоугольника
    #   изначально он равен сумме длин сторон
    def test_perimeter1(self):
        assert self.f.perimeter() == approx(2.0 + sqrt(2.0))

    #   добавление точки может его изменить
    def test_perimeter2(self):
        assert self.f.add(R2Point(1.0, 1.0)).perimeter() == approx(4.0)

    # Изменение площади многоугольника
    #   изначально она равна (неориентированной) площади треугольника
    def test_area1(self):
        assert self.f.area() == approx(0.5)

    #   добавление точки может увеличить площадь
    def test_area2(self):
        assert self.f.add(R2Point(1.0, 1.0)).area() == approx(1.0)

    # кол-во точек лежащих в 1 окрестности
    def test_snippet9(self):
        assert self.f.count() == 2.0

    # кол-во точек лежащих в 1 окрестности
    def test_snippet10(self):
        assert Polygon(R2Point(2.0, 2.5), R2Point(2.5, 2.0), R2Point(2.0, 2.0),
                       Snippet(R2Point(2, 2), R2Point(2, 2))).count() == 3.0

    # кол-во точек лежащих в 1 окрестности
    def test_snippet11(self):
        assert Polygon(self.a, self.b, self.c,
                       Snippet(R2Point(2, 2), R2Point(1, 0))).count() == 1.0
