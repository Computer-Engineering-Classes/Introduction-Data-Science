def make_bricks(small: int, big: int, goal: int) -> bool:
    b = goal // 5
    goal -= 5 * (b if b <= big else big)
    s = goal // 1
    goal -= s if s <= small else small
    return goal == 0


def lucky_sum(a: int, b: int, c: int) -> int:
    l = [a, b, c]
    try:
        i = l.index(13)
        l = l[:i]
        return sum(l)
    except ValueError:
        return sum(l)


def no_teen_sum(a: int, b: int, c: int) -> int:
    l = [0 if 13 <= x <= 19 and x not in [15, 16]
         else x for x in [a, b, c]]
    return sum(l)


def round_sum(a: int, b: int, c: int) -> int:
    l = [x - x % 10 if x % 10 < 5 else x + 10 - (x % 10)
         for x in [a, b, c]]
    return sum(l)


def close_far(a: int, b: int, c: int) -> bool:
    if abs(b - a) <= 1 and abs(c - a) >= 2 and abs(c - b) >= 2:
        return True
    elif abs(c - a) <= 1 and abs(b - a) >= 2 and abs(b - c) >= 2:
        return True
    else:
        return False


def lone_sum(a: int, b: int, c: int) -> int:
    s = 0
    if a != b and a != c:
        s += a
    if b != a and b != c:
        s += b
    if c != a and c != b:
        s += c
    return s


def make_chocolate(small: int, big: int, goal: int) -> int:
    b = goal // 5
    goal -= 5 * (b if b <= big else big)
    s = goal // 1
    s = s if s <= small else small
    goal -= s
    return s if goal == 0 else -1


if __name__ == "__main__":
    print(make_bricks(6, 1, 11))
