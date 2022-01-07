from classes import Points, Squares


# Check if given point is outside of a square
def is_outside(square, points):
    extrema_x = []
    for point in square.pts:
        extrema_x.append(point.x)
    extrema_x = [min(extrema_x), max(extrema_x)]
    
    extrema_y = []
    for point in square.pts:
        extrema_y.append(point.y)
    extrema_y = [min(extrema_y), max(extrema_y)]
    
    for point in points:
        if point in square.pts:
            continue

        if extrema_x[0] <= point.x <= extrema_x[1]:
            if extrema_y[0] <= point.y <= extrema_y[1]:
                return False
    
    return True


# Check if parallel square exists, then check if points are inside of it
# Mix point positions, so that there is only 1 call of is_outside function without billion IF statements
def find_square(squares, points):
    for square in squares:
        for pt in square.pts:
            for pt2 in square.pts:
                if pt2 != pt:
                    for pt3 in square.pts:
                        if pt3 not in [pt, pt2]:
                            for pt4 in square.pts:
                                if pt4 not in [pt, pt2, pt3]:
                                    if pt.x == pt2.x and pt3.x == pt4.x:
                                        if pt.y == pt4.y and pt2.y == pt3.y:
                                            if is_outside(square, points):
                                                return True
    return False


# Create instances of Points and Squares, then pass them as arguments one by one
def main():
    examples = (
        [(1, 1), (1, 5), (6, 5), (6, 1), (2, 3)],
        [(-1, 3), (-3, 1), (5, 3), (-3, 5)],
        [(-1, -1), (-1, -5), (-5, -5), (-5, -1), (-6, -2)],
        [(1, -1), (5, -1), (5, -5), (1, -5), (4, -2), (6, -2), (6, -4), (4, -4)],
        [(5, 6), (5, 9), (8, 9), (8, 6), (4, 5), (4, 10), (9, 10), (9, 5)],
        [(-1, 6), (-3, 6), (-3, 8), (-1, 8), (-2, 7), (-6, 7), (-6, 11), (-2, 11)]
    )

    for example in examples:
        # Input
        dane = example

        points = []

        for coords in dane:
            points.append(Points(coords[0], coords[1]))

        # Create all combinations of Squares from given Points, create instances
        squares = []
        for pt in points:
            for pt2 in points[points.index(pt):]:
                if pt2 != pt:
                    for pt3 in points[points.index(pt2):]:
                        if pt3 not in [pt, pt2]:
                            for pt4 in points[points.index(pt3):]:
                                if pt4 not in [pt, pt2, pt3]:
                                    squares.append(Squares(pt, pt2, pt3, pt4))

        print(find_square(squares, points))


if __name__ == "__main__":
    main()

# Example data: (Squares)

# [(1, 1), (1, 5), (6, 5), (6, 1), (2, 3)]  ->  False   ->   Square with point inside

# [(-1, 3), (-3, 1), (5, 3), (-3, 5)]   ->  False   -> Square is not parallel to OX and OY

# [(-1, -1), (-1, -5), (-5, -5), (-5, -1), (-6, -2)]    ->  True    ->  Square with no points inside

# [(1, -1), (5, -1), (5, -5), (1, -5), (4, -2), (6, -2), (6, -4), (4, -4)]  ->  True    -> 2 Squares, one is smaller

# [(5, 6), (5, 9), (8, 9), (8, 6), (4, 5), (4, 10), (9, 10), (9, 5)]    ->  2 Squares, one is inside another

# [(-1, 6), (-3, 6), (-3, 8), (-1, 8), (-2, 7), (-6, 7), (-6, 11), (-2, 11)]    ->  2 Squares, corners within each other
