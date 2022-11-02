from math import sqrt


def quadratic_equation(a: float, b: float, c: float):
    disc = discriminant(a=a, b=b, c=c)
    message = ""
    x1 = 0.0
    x2 = 0.0

    if disc == 0:
        x = (-b + sqrt(disc)) / (2 * a)
        x1 = x
        x2 = x
        message = "two repeated real roots"
    elif disc > 0:
        x1 = (-b + sqrt(disc)) / (2 * a)
        x2 = (-b - sqrt(disc)) / (2 * a)
        message = "two different real roots"
    else:
        message = "no real roots"

    return {"discriminant": disc, "x1": x1, "x2": x2, "message": message}


def discriminant(a: float, b: float, c: float):
    return pow(b, 2) - 4 * a * c
