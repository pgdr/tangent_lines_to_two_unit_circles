# Inner tangent line for two unit circle placed with centers at y = 0 and one in origo

This script computes the tangent point (and corresponding angle) for two
identical circles: one centered at $(0,0)$ and one centered at $(d,0)$.

One can find the tangent line by imagining a rectangle placed with
bottom left at $(0,0)$ (origo) and height $1$, with unknown length.


![](assets/rect.png)


Then rotate the rectangle until the top-right corner hits $(d,0)$.

This results in a triangle with hypothenus $d$, one leg has side $2$,
which gives (soh-**cah**-toa) $\cos(\theta) = 2/d$ and thus

$$\theta = \arccos(2/d).$$

![](assets/rect2.png)

Then, given $\theta$, we can find the tangent point on the first
(left-most) unit circle as simply the line with length 1 and given
angle. Here we piggy-back on the complex class in Python to find the
coordinates (real=x, imag=y), using `cmath.rect(r, theta)`.

## Usage

```bash
python tangent.py <d>
````

Example:

```bash
$ python tangent.py 5
```

outputs

```
tangent at (0.4, 0.917)
θ = 66.422°
Δ = ((0, 0), (0.4, 0.917), (2.5, 0))
```

The script prints:

* the tangent point on the left circle,
* $\theta$ in degrees,
* and a small helper triangle `Δ` for inspection.


## Code

```python
import math, cmath

def tangent_angle(d):
    theta = math.acos(2 / d)
    return theta

d = 5.0
theta = tangent_angle(d)
c = cmath.rect(1, theta)

print(f"tangent at {(c.real),(c.imag)}")
print(f"θ = {math.degrees(theta)}°")
print(f"Δ = ((0,0), {(c.real),(c.imag)}, {(d/2), 0})")
```
