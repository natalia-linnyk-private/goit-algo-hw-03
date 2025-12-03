import consts

def koch_curve(t, length, depth):
    if depth == consts.MIN_RECURSION_LEVEL:
        t.forward(length)
    else:
        length /= 3.0
        koch_curve(t, length, depth - 1)
        t.left(consts.ROTATION_ANGLE_60)
        koch_curve(t, length, depth - 1)
        t.right(consts.ROTATION_ANGLE_120)
        koch_curve(t, length, depth - 1)
        t.left(consts.ROTATION_ANGLE_60)
        koch_curve(t, length, depth - 1)

def koch_snowflake(t, length, depth):
    for _ in range(consts.DEFAULT_RECURSION_LEVEL):
        koch_curve(t, length, depth)
        t.right(consts.ROTATION_ANGLE_120)
