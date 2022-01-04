class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"


class Triangles:
    def __init__(self, pt, pt2, pt3):
        self.pt = pt
        self.pt2 = pt2
        self.pt3 = pt3
        self.pts = (pt, pt2, pt3)
        self.area = self.calc_area()

    def calc_area(self):
        return abs((self.pt.x * (self.pt2.y - self.pt3.y) + self.pt2.x * (self.pt3.y - self.pt.y)
                    + self.pt3.x * (self.pt.y - self.pt2.y)) / 2.0)

    def __repr__(self):
        return f"{self.pts}"


class Squares:
    def __init__(self, pt, pt2, pt3, pt4):
        self.pt = pt
        self.pt2 = pt2
        self.pt3 = pt3
        self.pt4 = pt4
        self.pts = (pt, pt2, pt3, pt4)

    def __repr__(self):
        return f"{self.pts}"
