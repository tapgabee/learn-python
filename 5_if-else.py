# in python use line indent to defind code block


def rectangle(w, h):  # dynamic typing
    return w * h


def triangle(w, h):
    return .5 * w * h


print('1. rectangle')
print('2. triangle')
n = input('select option:')
w = int(input('width = '))
h = int(input('height = '))

if n == '1':
    print('Rectangle area = ', rectangle(w, h))
else:
    print('Triangle area = ', triangle(w, h))
