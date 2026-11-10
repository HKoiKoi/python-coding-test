def solution(a, b, c):
    len_dice = len(set([a, b, c]))

    if len_dice == 1:
        return (3 * a) * (3 * a ** 2) * (3 * a ** 3)
    elif len_dice == 2:
        return (a + b + c) * (a ** 2 + b ** 2 + c ** 2)
    else:
        return a + b + c


test_cases = [
    ((2, 6, 1,), 9),
    ((5, 3, 3,), 473),
    ((4, 4, 4,), 110592),
]

for i, (args, expected) in enumerate(test_cases, 1):
    result = solution(*args)
    status = "정답" if result == expected else "오답"
    print(f"테스트 {i}: {status} (결과: {result!r}, 기대값: {expected!r})")
