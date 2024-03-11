import matplotlib.pyplot as plt
from math import sqrt, pi, atan, cos, sin
import itertools

def pairwise(iterable):
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)

def get_vector_angle(x, y):
    if x == 0:
        if y > 0:
            return pi / 2

        elif y < 0:
            return 3 * pi / 2

        else:
            raise ValueError("Not a vector")

    theta = atan(y / x)

    if x > 0 and y >= 0:
        return theta

    elif x < 0:
        return pi + theta

    elif x > 0 and y < 0:
        return 2 * pi + theta


def replace(p1, p2, pattern):
    x1, y1 = p1
    x2, y2 = p2
    dx, dy = x2 - x1, y2 - y1

    dv = sqrt(dx ** 2 + dy ** 2)
    dp = 1  # Should support non length 1 patterns?
    theta = get_vector_angle(dx, dy)  # Should support non horizontal patterns?

    res = []
    for x, y in pattern:
        # Should support non origin based patterns?
        xr, yr = x * dv / dp, y * dv / dp
        xr, yr = cos(theta) * xr - sin(theta) * yr, sin(theta) * xr + cos(theta) * yr
        xr, yr = x1 + xr, y1 + yr
        res.append((xr, yr))

    return res

# Koch snowflake
pattern = [(0, 0), (1/3, 0), (1/2, sqrt(3)/6), (2/3, 0), (1, 0)]
pattern = [(0, 0), (1/3, 0), (1/3, 1/4), (2/3, 1/4), (2/3, 0), (1, 0)]
pattern = [(0, 0), (1/2, 0), (1/2, 1/3), (1/2, 0), (1, 0)]



rounds = 10
points = [(0, 0), (100, 0)]

for _ in range(rounds):
    new_points = []
    for p1, p2 in pairwise(points):
        replacement = replace(p1, p2, pattern)

        for p in replacement[0:-1]:
            new_points.append(p)

    new_points.append(replacement[-1])
    points = new_points


xs, ys = [], []
for p in points:
    xs.append(p[0])
    ys.append(p[1])

plt.plot(xs, ys)

ax = plt.gca()
ax.set_aspect('equal', adjustable='box')

plt.show()
