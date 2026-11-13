from collections import Counter


def solution(a, b, c, d):
    count = Counter([a, b, c, d]).most_common()

    if len(count) == 4:
        return min(a, b, c, d)
    elif len(count) == 1:
        return 1111 * a
    elif len(count) == 3:
        return count[1][0] * count[2][0]
    else:
        p, count_p = count[0]
        q = count[1][0]

        if count_p == 2:
            return (p + q) * abs(p - q)
        else:
            return (10 * p + q) ** 2


test_cases = [
    ((2, 2, 2, 2,), 2222),
    ((4, 1, 4, 4,), 1681),
    ((6, 3, 3, 6,), 27),
    ((2, 5, 2, 6,), 30),
    ((6, 4, 2, 5,), 2),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
