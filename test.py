import math

def calculate():
    x1 = float(input('x1: '))
    z1 = float(input('z1: '))
    yaw1 = float(input('yaw1 (in Grad): '))
    x2 = float(input('x2: '))
    z2 = float(input('z2: '))
    yaw2 = float(input('yaw2 (in Grad): '))

    slope1 = -1 / math.tan(math.radians(yaw1))
    b1 = z1 - (x1 * slope1)
    slope2 = -1 / math.tan(math.radians(yaw2))
    b2 = z2 - (x2 * slope2)

    xpos = (b2 - b1) / (slope1 - slope2)
    zpos = xpos * slope1 + b1

    print(f'X, Z: ({xpos:.0f}, {zpos:.0f})')

# Benutzer kann die Werte für x1, z1, yaw1, x2, z2 und yaw2 eingeben
calculate()
