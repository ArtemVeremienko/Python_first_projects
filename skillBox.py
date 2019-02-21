import simple_draw as sd


point1 = sd.get_point(300, 100)
length1 = 100
angle1 = 90

def branche(point1, length1, angle1):
    if length1 < 2:
        return
    vector1 = sd.get_vector(point1, angle1, length1, 1)
    vector1.draw()

    point2 = vector1.end_point
    length2 = length1 * 0.7
    angle2 = angle1 - 30
    branche(point2, length2, angle2)
    angle3 = angle1 + 30
    branche(point2, length2, angle3)

branche(point1, length1, angle1)
sd.pause()


