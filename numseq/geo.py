def square(n):
    return n * n


def triangle(trial):
    balls = 0
    count = 0

    if trial == 0:
        return balls

    else:
        while trial >= count:

            balls = balls + count
            count += 1

        return balls


def cube(n):
    return pow(n, 3)
