# หาปีอธิกสุรทิน

# ค.ศ. % 4 : 0 = อธิกสุรทิน


def leap_year(year):
    if year % 4 == 0:
        return True
    else:
        return False

# พ.ศ. % 4 : 3 = อธิกสุรทิน


def leap_year_buddhist(year):
    if year % 4 == 3:
        return True
    else:
        return False

# เช็คเลขคู่


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

# เช็คเลขคี่


def is_odd(n):
    return not(is_even(n))

# โปรโมชัน


def promotion(come, pay, per_head, pax):
    return (pax // come) * (pay * per_head) + (pax % come) * per_head


print(leap_year(2019))
print(leap_year_buddhist(2560))

print(promotion(4, 2, 100, 6))
