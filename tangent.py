import sys
import math


def R(v, digits=3):
    return round(v, digits)


def tangent_angle(d):
    theta = math.acos(2 / d)
    return theta


if __name__ == "__main__":
    if len(sys.argv) != 2:
        exit("usage: tangent.py d")
    d = float(sys.argv[1])
    theta = tangent_angle(d)
    print(f"θ = {R(theta)} = {R(math.degrees(theta))}°")
    print(f"cos θ = 2/d = 2/{d} = {R(2/d)}")
    print(
        f"sin θ = √(d^2 - 4)/d = √({d}^2 - 4)/{d} = √({R(d**2) - 4})/{d} = {R(math.sqrt(d**2 - 4)/d)}"
    )
    print(f"p = (cos θ, sin θ) = {R(2/d), R(math.sqrt(d**2 - 4)/d)}")
