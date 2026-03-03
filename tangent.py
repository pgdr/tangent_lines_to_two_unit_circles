import sys
import math
import cmath


def R(v, digits=3):
    return round(v, digits)


def tangent_angle(d):
    theta = math.acos(2 / d)
    return theta


if len(sys.argv) != 2:
    exit("usage: tangent.py d")

d = float(sys.argv[1])
theta = tangent_angle(d)
c = cmath.rect(1, theta)

print(f"tangent at {(R(c.real), R(c.imag))}")
print(f"θ = {R(math.degrees(theta))}°")
print(f"Δ = ((0, 0), {(R(c.real), R(c.imag))}, {(R(d/2), 0)})")
