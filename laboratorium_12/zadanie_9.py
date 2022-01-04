from classes import Points, Triangles


# Check if given point is outside of a triangle (Calc area from Heron's formula)
def is_outside(triangle, points):

    for point in points:
        if point in [triangle.pt, triangle.pt2, triangle.pt3]:
            continue

        p12 = Triangles(triangle.pt, triangle.pt2, point)
        p13 = Triangles(triangle.pt, triangle.pt3, point)
        p23 = Triangles(triangle.pt2, triangle.pt3, point)

        if triangle.area == (p12.area + p13.area + p23.area):
            return False

    return True


# Check if triangle is parallel to OX and OY => is a right triangle
def find_triangle(triangles, points):
    for triangle in triangles:
        if triangle.pt.x == triangle.pt2.x:
            if triangle.pt.y == triangle.pt3.y or triangle.pt2.y == triangle.pt3.y:
                if is_outside(triangle, points):
                    return True

        elif triangle.pt.x == triangle.pt3.x:
            if triangle.pt.y == triangle.pt2.y or triangle.pt3.y == triangle.pt2.y:
                if is_outside(triangle, points):
                    return True

        elif triangle.pt2.x == triangle.pt3.x:
            if triangle.pt2.y == triangle.pt.y or triangle.pt3.y == triangle.pt.y:
                if is_outside(triangle, points):
                    return True
    return False


'''
Optional code for above (point positions are mixed so that there is only 1 is_outside call):

        for pt in triangle.pts:
            for pt2 in triangle.pts:
                if pt != pt2:
                    for pt3 in triangle.pts:
                        if pt3 not in [pt, pt2]:
                            if pt.x == pt2.x and (pt.y == pt3.y or pt2.y == pt3.y):
                                if is_outside(triangle, points):
                                    return True

    return False
'''


# Create instances of Points and Triangles, then pass them as arguments one by one
def main():
    examples = (
        [(1, 1), (3, 1), (1, 6), (2, 2)],
        [(-1, 3), (-3, 1), (-6, 4)],
        [(-1, -1), (-5, -1), (-1, -6), (-4, -4)],
        [(1, -3), (3, -1), (3, -3), (2, -1), (2, -5), (5, -5)],
        [(4, 2), (4, 6), (7, 6), (3, 4), (6, 4), (6, 7)],
        [(-2, 5), (-6, 8), (-2, 8), (-3, 7), (-3, 10), (-1, 7)]
    )

    for example in examples:
        # Input
        dane = example

        points = []

        for coords in dane:
            points.append(Points(coords[0], coords[1]))

        # Create all combinations of Triangles from given Points, create instances
        triangles = []
        for pt in points:
            for pt2 in points[points.index(pt):]:
                for pt3 in points[points.index(pt2):]:
                    if pt not in [pt2, pt3] and pt2 != pt3:
                        triangles.append(Triangles(pt, pt2, pt3))
                    else:
                        continue

        print(find_triangle(triangles, points))


if __name__ == "__main__":
    main()


# Example data: (Triangles)

# [(1, 1), (3, 1), (1, 6), (2, 2)]  ->  False   ->  Prostokątny, Punkt w środku

# [(-1, 3), (-3, 1), (-6, 4)]   ->  False   ->  Prostokątny, nie równoległy do osi

# [(-1, -1), (-5, -1), (-1, -6), (-4, -4)]  ->  True    ->  Prostokątny, Punkt na zewnątrz

# [(1, -3), (3, -1), (3, -3), (2, -1), (2, -5), (5, -5)]   ->   True    ->  2 Prostokątne, Jeden zawiera drugi

# [(4, 2), (4, 6), (7, 6), (3, 4), (6, 4), (6, 7)]  ->  True    ->  2 Prostokątne, Trójkąty nie nachodzą na siebie

# [(-2, 5), (-6, 8), (-2, 8), (-3, 7), (-3, 10), (-1, 7)]  ->   False   ->  Prostokątne, Zawierają się w sobie
