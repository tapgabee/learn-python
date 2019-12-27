# in python use line indent to defind code block


def rectangle(w, h):  # dynamic typing
    return w * h


def triangle(w, h):
    return .5 * w * h


w = int(input('width = '))
h = int(input('height = '))
print('Rectangle area = ', rectangle(w, h))
print('Triangle area = ', triangle(w, h))
